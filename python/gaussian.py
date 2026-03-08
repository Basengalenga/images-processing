from PIL import Image
import sys

def gaussian_kernel():
    return [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]

def get_pixel_clamped(pixels, x, y, width, height):
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    return pixels[x, y]

def apply_gaussian(image_path, output_path="gaussian_output.png"):
    img = Image.open(image_path).convert("L")  # Grayscale
    pixels = img.load()
    width, height = img.size
    kernel = gaussian_kernel()
    kernel_sum = 16

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            val = 0
            for ky in range(3):
                for kx in range(3):
                    px = get_pixel_clamped(pixels, x + kx - 1, y + ky - 1, width, height)
                    val += px * kernel[ky][kx]
            new_pixels[x, y] = val // kernel_sum

    new_img.save(output_path)
    print(f"Gaussian filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "gaussian_output.png"
    apply_gaussian(image_path, output_path)