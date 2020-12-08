from pathlib import Path

import numpy as np


def parse_program(fpath):
    program = []
    with fpath.open() as f:
        for r in f.readlines():
            cmd, val = r.strip().split(" ")
            program.append((cmd, int(val)))
    return program


def run_program(program, substitute={}):
    """ Run the program for the game console.

    Parameters
    ----------
    program: iterable of (cmd, value) tuples
    substitute: dict of {substitute_index: substitute_cmd}

    Returns
    -------
    exit_code : int
        0 for success, 99 for infinite loop
    accumulator : int
    """
    line_runs = np.zeros(len(program))
    accumulator = 0
    i = 0
    while i < len(program):
        line_runs[i] += 1
        if line_runs[i] == 2:
            return 99, accumulator
        cmd, val = program[i]
        cmd = substitute.get(i, cmd)
        if cmd == "acc":
            accumulator += val
        if cmd == "jmp":
            i += val
            continue
        i += 1
    else:
        return 0, accumulator


if __name__ == "__main__":  
    program = parse_program(Path(__file__).parent / "input.txt")
    exit_code, accumulator = run_program(program)
    if exit_code == 99:
        print(accumulator)
    else:
        print("program ran successfully?")
