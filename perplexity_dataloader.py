import numpy as np
import rasterio

class GeoTiffDataLoader:
    def __init__(self, file_path, tile_size):
        self.file_path = file_path
        self.tile_size = tile_size
        self.dataset = rasterio.open(file_path)
        self.width = self.dataset.width
        self.height = self.dataset.height

    def get_random_tile(self):
        x = np.random.randint(0, self.width - self.tile_size)
        y = np.random.randint(0, self.height - self.tile_size)
        tile = self.dataset.read(window=((y, y + self.tile_size), (x, x + self.tile_size)))
        return tile
