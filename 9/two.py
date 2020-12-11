import sys
from pathlib import Path

import numpy as np

from one import find_flaw


if __name__ == "__main__":  
    data = np.loadtxt(Path(__file__).parent / "input.txt", dtype=int)
    flaw = find_flaw(data, pre=25)

    for i in range(len(data)):
        cumulative = np.cumsum(data[i:])
        matching = (flaw == cumulative)
        if np.any(matching):
            sub_index = np.argwhere(matching)[0][0]
            if sub_index:
                numbers = data[i:i + sub_index + 1]
                print(numbers.min() + numbers.max())