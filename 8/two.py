import sys
from pathlib import Path

import numpy as np

from one import parse_program, run_program


if __name__ == "__main__":  
    program = parse_program(Path(__file__).parent / "input.txt")

    for sub_i, (sub_cmd, _) in enumerate(program):
        sub_cmd = {"nop": "jmp", "jmp": "nop"}.get(sub_cmd)
        if sub_cmd is None:
            continue
        exit_code, accumulator = run_program(program, substitute={sub_i: sub_cmd})    
        if exit_code == 0:
            break
    print(accumulator)
