import numpy as np
import pygame as pg

from constants import consts as c
from images import img as i


class Grid:
    def __init__(self):
        self.grid = np.zeros((c.num_cells, c.num_cells), dtype=int)

        self.sprite_locations = []

    def update(self, entity, loc):
        if self.grid[loc] == 0:
            self.grid[loc] = entity
            self.sprite_locations.append(loc)

    def toggle_rotation(self, loc):
        if self.grid[loc] != 0:
            self.grid[loc] += 1
            if self.grid[loc] > 4:
                self.grid[loc] = 1

    def destroy(self, loc):
        self.grid[loc] = 0
        if loc in self.sprite_locations:
            self.sprite_locations.remove(loc)

    def render(self):
        for loc in self.sprite_locations:
            if self.grid[loc] != 0:
                row, col = loc
                x = col * c.cell_length - c.player_x
                y = row * c.cell_length - c.player_y
                c.screen.blit(i.images[self.grid[loc] - 1], (x, y))

    def is_conveyor(self, loc):
        return 0 < self.grid[loc] < 5


grid = Grid()