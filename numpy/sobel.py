import numpy as np
from PIL import Image
import sys

def apply_sobel(image_path, output_path="sobel_output.png"):
    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)

    Kx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    Ky = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=np.float32)

    padded = np.pad(pixels, 1, mode='edge')
    sx = np.zeros_like(pixels)
    sy = np.zeros_like(pixels)

    for ky in range(3):
        for kx in range(3):
            region = padded[ky:ky+pixels.shape[0], kx:kx+pixels.shape[1]]
            sx += region * Kx[ky, kx]
            sy += region * Ky[ky, kx]

    magnitude = np.clip(np.sqrt(sx**2 + sy**2), 0, 255).astype(np.uint8)
    Image.fromarray(magnitude).save(output_path)
    print(f"Sobel filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sobel_output.png"
    apply_sobel(image_path, output_path)