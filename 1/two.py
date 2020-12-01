import numpy as np

from one import sym_sum

if __name__ == "__main__":
    arr = np.loadtxt("input.txt", dtype=int)
    out, x, y = sym_sum(arr)
    i, j = np.argwhere((out[:, np.newaxis] + arr[np.newaxis, :]) == 2020)[0]
    print(x[i] * y[i] * arr[j])

