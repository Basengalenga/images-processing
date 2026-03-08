from PIL import Image
import sys

def get_pixel_clamped(pixels, x, y, width, height):
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    return pixels[x, y]

def apply_median(image_path, output_path="median_output.png"):
    img = Image.open(image_path).convert("L")  # Grayscale
    pixels = img.load()
    width, height = img.size

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            vals = []
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    vals.append(get_pixel_clamped(pixels, x + kx, y + ky, width, height))
            vals.sort()
            new_pixels[x, y] = vals[4]  # median of 9 = index 4

    new_img.save(output_path)
    print(f"Median filter applied. Saved to {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "input.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "median_output.png"
    apply_median(image_path, output_path)