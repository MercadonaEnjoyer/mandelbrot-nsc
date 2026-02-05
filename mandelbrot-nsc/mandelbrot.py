import numpy as np
import matplotlib.pyplot as plt
import time

def mandelbrot(rows, cols, max_iter=200):
    x = np.linspace(-2, 1, cols)
    y = np.linspace(-1.5, 1.5, rows)
    screen = x + y[:, None]*1j  

    iter_count = np.zeros((rows, cols), dtype=np.int16)

    for i in range(rows):
        for j in range(cols):
            z = 0 + 0j
            for k in range(max_iter):
                z = z**2 + screen[i, j]
                if abs(z) > 2:
                    break
            iter_count[i, j] = k 

    return iter_count

if __name__ == "__main__":
    rows, cols = 1000, 1000
    start = time.time()
    mandelbrot_image = mandelbrot(rows, cols)
    end = time.time()

    final_time = end-start
    print(final_time)

    plt.imshow(mandelbrot_image, cmap='hot', interpolation='nearest')
    plt.axis('off')
    plt.show()
