from pathlib import Path


if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    total = 0
    with fpath.open() as f:
        questions = None
        for r in f.readlines():
            r = r.strip()
            if not r:
                total += len(questions) if questions is not None else 0
                questions = None
                continue
            if questions is None:
                questions = set([l for l in r])
                continue
            questions &= set([l for l in r])
        else:
            total += len(questions) if questions is not None else 0
    print(total)
