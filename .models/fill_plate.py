import sys
import numpy as np
from PIL import Image, ImageFilter

def main(full_path, cutout_path, offset_x, offset_y, out_path):
    full = Image.open(full_path).convert("RGB")
    fw, fh = full.size
    full_arr = np.array(full).astype(np.float32)

    cutout = Image.open(cutout_path)
    alpha = np.array(cutout.split()[-1]).astype(np.float32)  # 0..255
    cw, ch = cutout.size

    # Binary hole mask in crop-local coords, slightly dilated so no soft
    # rider-edge ghost survives in the fill.
    hole = (alpha > 25).astype(np.uint8)
    hole_img = Image.fromarray(hole * 255, mode="L").filter(ImageFilter.MaxFilter(9))
    hole = (np.array(hole_img) > 0)

    ox, oy = offset_x, offset_y
    BUF = 6  # sample this many px further out to skip any residual feather

    for row in range(ch):
        row_mask = hole[row]
        if not row_mask.any():
            continue
        # find contiguous runs of True in row_mask
        idx = np.where(row_mask)[0]
        runs = []
        start = idx[0]
        prev = idx[0]
        for v in idx[1:]:
            if v != prev + 1:
                runs.append((start, prev))
                start = v
            prev = v
        runs.append((start, prev))

        fy = oy + row
        if fy < 0 or fy >= fh:
            continue

        for (rs, re) in runs:
            left_x = ox + rs - BUF
            right_x = ox + re + BUF
            n = re - rs + 1
            if left_x >= 0 and right_x < fw:
                left_col = full_arr[fy, left_x]
                right_col = full_arr[fy, right_x]
                t = np.linspace(0, 1, n)[:, None]
                fill = left_col[None, :] * (1 - t) + right_col[None, :] * t
            elif left_x >= 0:
                fill = np.tile(full_arr[fy, left_x], (n, 1))
            elif right_x < fw:
                fill = np.tile(full_arr[fy, right_x], (n, 1))
            else:
                continue
            full_arr[fy, ox + rs: ox + re + 1] = fill

    out = Image.fromarray(np.clip(full_arr, 0, 255).astype(np.uint8), mode="RGB")
    out.save(out_path, quality=95)
    print("saved", out_path, out.size)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
