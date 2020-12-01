import numpy as np

def sym_sum(v):
    out = v[:, np.newaxis] + v[np.newaxis, :]
    upper_half = np.triu_indices(out.shape[0], k=1)
    return out[upper_half], v[upper_half[0]], v[upper_half[1]]

if __name__ == "__main__":
    v = np.loadtxt("input.txt", dtype=int)
    out, x, y = sym_sum(v)
    i = int(np.argwhere(out==2020))
    print(x[i] * y[i])

