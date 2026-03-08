from PIL import Image
import math
import sys

def get_pixel_clamped(pixels, x, y, width, height):
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    return pixels[x, y]

def apply_sobel(image_path, output_path="sobel_output.png"):
    img = Image.open(image_path).convert("L")  # Grayscale
    pixels = img.load()
    width, height = img.size

    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    Ky = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            sx, sy = 0, 0
            for ky in range(3):
                for kx in range(3):
                    p = get_pixel_clamped(pixels, x + kx - 1, y + ky - 1, width, height)
                    sx += p * Kx[ky][kx]
                    sy += p * Ky[ky][kx]
            magnitude = min(int(math.sqrt(sx**2 + sy**2)), 255)
            new_pixels[x, y] = magnitude

    new_img.save(output_path)
    print(f"Sobel filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sobel_output.png"
    apply_sobel(image_path, output_path)