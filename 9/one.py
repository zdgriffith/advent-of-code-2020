import sys
from pathlib import Path

import numpy as np


def find_flaw(data, pre=25):
    i = pre
    while i < len(data):
        subset = data[i-pre:i]
        combos = subset[:, np.newaxis] + subset[np.newaxis, :]
        if not np.any(data[i] == combos):
            return data[i]
        i += 1


if __name__ == "__main__":  
    data = np.loadtxt(Path(__file__).parent / "input.txt", dtype=int)
    print(find_flaw(data, pre=25))
