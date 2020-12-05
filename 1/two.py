from pathlib import Path

import numpy as np

from one import sym_sum

if __name__ == "__main__":
    fpath = Path(__file__).parent / "input.txt"
    arr = np.loadtxt(fpath, dtype=int)
    out, x, y = sym_sum(arr)
    i, j = np.argwhere((out[:, np.newaxis] + arr[np.newaxis, :]) == 2020)[0]
    print(x[i] * y[i] * arr[j])

