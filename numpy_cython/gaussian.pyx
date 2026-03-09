import numpy as np
cimport numpy as np

def apply_gaussian(str image_path, str output_path="gaussian_output.png"):
    from PIL import Image

    cdef np.ndarray[np.float32_t, ndim=2] pixels, output, padded
    cdef np.ndarray[np.float32_t, ndim=2] kernel
    cdef int ky, kx, h, w

    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)
    h, w = pixels.shape[0], pixels.shape[1]

    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=np.float32) / 16.0

    padded = np.pad(pixels, 1, mode='edge')
    output = np.zeros((h, w), dtype=np.float32)

    for ky in range(3):
        for kx in range(3):
            output += padded[ky:ky+h, kx:kx+w] * kernel[ky, kx]

    result = np.clip(output, 0, 255).astype(np.uint8)
    Image.fromarray(result).save(output_path)
    print(f"Gaussian filter applied. Saved to {output_path}")
