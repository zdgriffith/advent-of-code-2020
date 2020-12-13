from pathlib import Path

import numpy as np


def parse_directions(fpath):
    directions = []
    with fpath.open() as f:
        for r in f.readlines():
            r = r.strip()
            directions.append((r[0], int(r[1:])))
    return directions

dirs = {
    "E": np.array([1, 0]),
    "S": np.array([0, -1]),
    "W": np.array([-1, 0]),
    "N": np.array([0, 1]),
}

class Ship:
    def __init__(self, direction=[1, 0], loc=(0, 0), use_waypoint=False):
        self.dir = np.array(direction)
        self.loc = np.array(loc)
        self.use_waypoint = use_waypoint

    def change_dir(self, cmd, value):
        reverse = 1 if cmd == "R" else -1
        if value == 90:
            self.dir = reverse * np.array([self.dir[1], -self.dir[0]])
        elif value == 180:
            self.dir = -self.dir
        elif value == 270:
            self.dir = reverse * np.array([-self.dir[1], self.dir[0]])

    def move(self, cmd, value):
        if cmd in dirs:
            if self.use_waypoint:
                self.dir += dirs[cmd] * value
            else:
                self.loc += dirs[cmd] * value
        elif cmd == "F":
            self.loc += self.dir * value
        elif cmd in ["L", "R"]:
            self.change_dir(cmd, value)
        else:
            raise ValueError("invalid command!")

    @property
    def distance(self):
        return np.abs(self.loc).sum()

if __name__ == "__main__":  
    directions = parse_directions(Path(__file__).parent / "input.txt")
    ship = Ship()
    for cmd, value in directions:
        ship.move(cmd, value)
    print(ship.distance)