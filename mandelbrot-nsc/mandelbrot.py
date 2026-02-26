import numpy as np
import matplotlib.pyplot as plt
import time

def mandelbrot(rows, cols, max_iter=200):
    # Complex grid
    x = np.linspace(-2, 1, cols)
    y = np.linspace(-1.5, 1.5, rows)
    C = x + y[:, None] * 1j

    Z = np.zeros_like(C, dtype=np.complex128)
    iter_count = np.zeros(C.shape, dtype=np.int16)

    # Boolean mask: True where still computing
    mask = np.ones(C.shape, dtype=bool)

    for k in range(max_iter):
        # Apply iteration only to active points
        Z[mask] = Z[mask]**2 + C[mask]

        # Points that escaped in this iteration
        escaped = np.abs(Z) > 2

        # Store iteration number for newly escaped points
        newly_escaped = escaped & mask
        iter_count[newly_escaped] = k

        # Remove escaped points from further computation
        mask &= ~escaped

        # Early exit if all points escaped
        if not mask.any():
            break

    return iter_count


if __name__ == "__main__":
    rows, cols = 1000, 1000
    start = time.time()
    mandelbrot_image = mandelbrot(rows, cols)
    end = time.time()

    print(end - start)

    plt.imshow(mandelbrot_image, cmap='twilight', interpolation='nearest')
    plt.axis('off')
    plt.show()