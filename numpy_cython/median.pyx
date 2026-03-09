import numpy as np
cimport numpy as np

def apply_median(str image_path, str output_path="median_output.png"):
    from PIL import Image

    cdef np.ndarray[np.float32_t, ndim=2] pixels, padded
    cdef int h, w

    img = Image.open(image_path).convert("L")
    pixels = np.array(img, dtype=np.float32)
    h, w = pixels.shape[0], pixels.shape[1]

    padded = np.pad(pixels, 1, mode='edge')

    neighbors = np.stack([
        padded[ky:ky+h, kx:kx+w]
        for ky in range(3)
        for kx in range(3)
    ], axis=0)

    output = np.median(neighbors, axis=0).astype(np.uint8)
    Image.fromarray(output).save(output_path)
    print(f"Median filter applied. Saved to {output_path}")
