import sys
from pathlib import Path

import numpy as np


if __name__ == "__main__":  
    data = np.sort(np.loadtxt(Path(__file__).parent / "input.txt", dtype=int))
    diff = np.diff(np.array([0] + list(data) + [3 + data.max()]))
    print(np.sum(diff == 1) * (np.sum(diff == 3)))
