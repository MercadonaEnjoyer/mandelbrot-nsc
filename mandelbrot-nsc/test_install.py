# test_install.py

import sys
import numpy
import scipy
import matplotlib
import numba
import pytest
import dask

# Add more packages as needed

def print_versions():
    print("Python:", sys.version)
    print("NumPy:", numpy.__version__)
    print("SciPy:", scipy.__version__)
    print("Matplotlib:", matplotlib.__version__)
    print("Numba:", numba.__version__)
    print("Numba:", pytest.__version__)
    print("Numba:", dask.__version__)

if __name__ == "__main__":
    print_versions()
