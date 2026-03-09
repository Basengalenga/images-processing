import numpy as np
from PIL import Image
import sys

def gaussian_kernel():
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=np.float32)
    return kernel / 16.0

def apply_gaussian(image_path, output_path="gaussian_output.png"):
    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)
    kernel = gaussian_kernel()

    padded = np.pad(pixels, 1, mode='edge')
    output = np.zeros_like(pixels)

    for ky in range(3):
        for kx in range(3):
            output += padded[ky:ky+pixels.shape[0], kx:kx+pixels.shape[1]] * kernel[ky, kx]

    output = np.clip(output, 0, 255).astype(np.uint8)
    Image.fromarray(output).save(output_path)
    print(f"Gaussian filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "gaussian_output.png"
    apply_gaussian(image_path, output_path)