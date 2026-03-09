import numpy as np
from PIL import Image
import sys

def apply_median(image_path, output_path="median_output.png"):
    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)

    padded = np.pad(pixels, 1, mode='edge')
    height, width = pixels.shape
    output = np.zeros_like(pixels)

    # Stack all 9 neighbors into a 3D array and take median
    neighbors = np.stack([
        padded[ky:ky+height, kx:kx+width]
        for ky in range(3)
        for kx in range(3)
    ], axis=0)

    output = np.median(neighbors, axis=0).astype(np.uint8)
    Image.fromarray(output).save(output_path)
    print(f"Median filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "median_output.png"
    apply_median(image_path, output_path)