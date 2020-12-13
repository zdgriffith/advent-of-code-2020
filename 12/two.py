from pathlib import Path

import numpy as np

from one import parse_directions, dirs, Ship


if __name__ == "__main__":  
    directions = parse_directions(Path(__file__).parent / "input.txt")
    ship = Ship(direction=[10, 1], use_waypoint=True)
    for cmd, value in directions:
        ship.move(cmd, value)
    print(ship.distance)
