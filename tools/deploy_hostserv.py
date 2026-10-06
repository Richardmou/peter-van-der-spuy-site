"""Upload the built site to petervanderspuy.com (Hostserv cPanel) over FTPS.

Reads FTP_HOST, FTP_USER, FTP_PASS from .env at the project root. Uploads only
files whose SHA-1 changed since the last deploy (manifest in
tools/.deploy_manifest.json). Never deletes anything on the server.

  python tools/deploy_hostserv.py             # upload changed files
  python tools/deploy_hostserv.py --dry-run   # list what would upload
  python tools/deploy_hostserv.py --full      # ignore manifest, upload all
  python tools/deploy_hostserv.py --retire-wordpress --full
      # one-off: move the old WordPress site into _old_wordpress/ (web access
      # denied) before uploading. Backups: Peter Hosting/wp-backup + .sql
  python tools/deploy_hostserv.py --lock-retired   # rewrite only the deny rule
"""
import ftplib, hashlib, io, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scrollcraft", "builds", "peter-van-der-spuy")
MANIFEST = os.path.join(ROOT, "tools", ".deploy_manifest.json")
TOP = [".htaccess", "index.html", "scrollcraft.css", "scrollcraft.js", "robots.txt", "sitemap.xml"]
RETIRED = "_old_wordpress"
KEEP_ON_RETIRE = {".", "..", ".well-known", "cgi-bin", ".ftpquota", RETIRED}
DIRS = ["assets", "blog"]
SKIP_DIRS = {"_originals"}
SKIP_EXT = {".md"}


def load_env():
    env = {}
    with open(os.path.join(ROOT, ".env"), encoding="utf-8") as f:
        for line in f:
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.strip().split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env


def site_files():
    for f in TOP:
        yield f
    for d in DIRS:
        for root, ds, fs in os.walk(os.path.join(SRC, d)):
            ds[:] = [x for x in ds if x not in SKIP_DIRS]
            for f in fs:
                if os.path.splitext(f)[1] not in SKIP_EXT:
                    yield os.path.relpath(os.path.join(root, f), SRC).replace("\\", "/")


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def ensure_dir(ftp, remote_dir, made):
    if remote_dir in made or not remote_dir:
        return
    parts = remote_dir.split("/")
    for i in range(1, len(parts) + 1):
        d = "/".join(parts[:i])
        if d in made:
            continue
        try:
            ftp.mkd(d)
        except ftplib.error_perm:
            pass  # already exists
        made.add(d)


def lock_retired(ftp):
    # Written after the move: WordPress's own .htaccess moves into the same
    # folder and would otherwise replace this one.
    ftp.storbinary(f"STOR {RETIRED}/.htaccess", io.BytesIO(b"Require all denied\n"))
    print(f"{RETIRED}/ locked")


def retire_wordpress(ftp):
    try:
        ftp.mkd(RETIRED)
    except ftplib.error_perm:
        pass  # already exists
    moved = 0
    for name in ftp.nlst():
        name = name.rsplit("/", 1)[-1]
        if name not in KEEP_ON_RETIRE:
            ftp.rename(name, f"{RETIRED}/{name}")
            moved += 1
    print(f"moved {moved} WordPress entries into {RETIRED}/")
    lock_retired(ftp)


def main():
    dry, full = "--dry-run" in sys.argv, "--full" in sys.argv
    retire = "--retire-wordpress" in sys.argv
    if "--lock-retired" in sys.argv:
        env = load_env()
        ftp = ftplib.FTP_TLS(env["FTP_HOST"], timeout=60)
        ftp.login(env["FTP_USER"], env["FTP_PASS"])
        ftp.prot_p()
        lock_retired(ftp)
        ftp.quit()
        return
    old = {}
    if not full and os.path.exists(MANIFEST):
        with open(MANIFEST) as f:
            old = json.load(f)
    new = {p: sha1(os.path.join(SRC, p)) for p in site_files()}
    todo = [p for p in new if old.get(p) != new[p]]
    print(f"{len(todo)} of {len(new)} files to upload")
    if dry or not todo:
        for p in todo:
            print("  ", p)
        return
    env = load_env()
    ftp = ftplib.FTP_TLS(env["FTP_HOST"], timeout=60)
    ftp.login(env["FTP_USER"], env["FTP_PASS"])
    ftp.prot_p()
    if retire:
        retire_wordpress(ftp)
    made = set()
    for i, p in enumerate(todo, 1):
        ensure_dir(ftp, os.path.dirname(p), made)
        with open(os.path.join(SRC, p), "rb") as f:
            ftp.storbinary(f"STOR {p}", f)
        old[p] = new[p]
        with open(MANIFEST, "w") as f:
            json.dump(old, f)
        print(f"  [{i}/{len(todo)}] {p}")
    ftp.quit()
    print("done")


if __name__ == "__main__":
    main()
