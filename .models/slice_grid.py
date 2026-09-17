import sys
import numpy as np
from PIL import Image

def find_grid_rows(arr, white_thresh=245, row_white_frac_thresh=0.4):
    # arr: HxWx3 uint8. A "grid content" row has very few near-white pixels
    # across its full width (photos butt up edge-to-edge); header/bio rows
    # are mostly white background.
    whiteish = np.all(arr > white_thresh, axis=2)
    frac_white = whiteish.mean(axis=1)
    is_content = frac_white < row_white_frac_thresh
    return is_content

def runs_of_true(mask):
    runs = []
    in_run = False
    start = 0
    for i, v in enumerate(mask):
        if v and not in_run:
            start = i
            in_run = True
        elif not v and in_run:
            runs.append((start, i - 1))
            in_run = False
    if in_run:
        runs.append((start, len(mask) - 1))
    return runs

def main(src_path, out_prefix, cols=3, rows=4):
    img = Image.open(src_path).convert("RGB")
    arr = np.array(img)
    h, w, _ = arr.shape

    is_content = find_grid_rows(arr)
    runs = runs_of_true(is_content)
    # keep only substantial runs (real photo rows, not stray icon/button rows)
    runs = [r for r in runs if (r[1] - r[0]) > 100]
    if not runs:
        print("no grid rows found")
        return

    grid_top = runs[0][0]
    grid_bottom = runs[-1][1]
    print(f"grid region rows: {grid_top}..{grid_bottom} (h={h})")

    # Reels tiles render taller than wide (~4:5), and internal light patches
    # (white caption cards baked into some thumbnails) make gap-based row
    # splitting unreliable, so just divide the detected block evenly into
    # a known row count instead of trying to detect each row's own band.
    row_h = (grid_bottom - grid_top) / rows
    row_bands = [
        (int(grid_top + i * row_h), int(grid_top + (i + 1) * row_h))
        for i in range(rows)
    ]
    print("row bands:", row_bands)

    # Detect the grid's horizontal extent the same way: scan columns within
    # the full content block for where near-white drops off.
    top_all, bot_all = row_bands[0][0], row_bands[-1][1]
    strip = arr[top_all:bot_all]
    whiteish_col = np.all(strip > 245, axis=2)
    frac_white_col = whiteish_col.mean(axis=0)
    content_cols = np.where(frac_white_col < 0.3)[0]
    grid_left, grid_right = int(content_cols.min()), int(content_cols.max())
    print(f"grid cols: {grid_left}..{grid_right} (w={w})")

    col_w = (grid_right - grid_left) / cols
    count = 0
    for (rtop, rbot) in row_bands:
        for c in range(cols):
            x0 = grid_left + int(c * col_w) + 2
            x1 = grid_left + int((c + 1) * col_w) - 2
            y0 = rtop + 2
            y1 = rbot - 2
            if y1 - y0 < 40 or x1 - x0 < 40:
                continue
            tile = img.crop((x0, y0, x1, y1))
            count += 1
            out_path = f"{out_prefix}_{count:02d}.jpg"
            tile.save(out_path, quality=90)
    print("saved", count, "tiles")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
