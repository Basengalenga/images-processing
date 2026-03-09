import numpy as np
cimport numpy as np

def apply_sobel(str image_path, str output_path="sobel_output.png"):
    from PIL import Image

    cdef np.ndarray[np.float32_t, ndim=2] pixels, sx, sy, padded
    cdef int ky, kx, h, w

    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)
    h, w = pixels.shape[0], pixels.shape[1]

    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    padded = np.pad(pixels, 1, mode='edge')
    sx = np.zeros((h, w), dtype=np.float32)
    sy = np.zeros((h, w), dtype=np.float32)

    for ky in range(3):
        for kx in range(3):
            region = padded[ky:ky+h, kx:kx+w]
            sx += region * Kx[ky, kx]
            sy += region * Ky[ky, kx]

    magnitude = np.clip(np.sqrt(sx**2 + sy**2), 0, 255).astype(np.uint8)
    Image.fromarray(magnitude).save(output_path)
    print(f"Sobel filter applied. Saved to {output_path}")
