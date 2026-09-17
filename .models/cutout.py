import sys
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageFilter

def main(src_path, out_path, model_path):
    session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    input_name = session.get_inputs()[0].name

    img = Image.open(src_path).convert("RGB")
    orig_w, orig_h = img.size

    # U2Net expects 320x320, normalized with ImageNet-ish mean/std used by rembg.
    resized = img.resize((320, 320), Image.LANCZOS)
    arr = np.asarray(resized).astype(np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    arr = (arr - mean) / std
    arr = arr.transpose(2, 0, 1)[np.newaxis, :, :, :].astype(np.float32)

    outputs = session.run(None, {input_name: arr})
    pred = outputs[0][0][0]  # (320, 320) saliency map

    pred = (pred - pred.min()) / (pred.max() - pred.min() + 1e-8)
    mask = Image.fromarray((pred * 255).astype(np.uint8), mode="L").resize(
        (orig_w, orig_h), Image.LANCZOS
    )
    # Soften edges slightly so the cutout doesn't look laser-cut.
    mask = mask.filter(ImageFilter.GaussianBlur(radius=2))

    rgba = img.convert("RGBA")
    rgba.putalpha(mask)
    rgba.save(out_path)
    print("saved", out_path, rgba.size)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
