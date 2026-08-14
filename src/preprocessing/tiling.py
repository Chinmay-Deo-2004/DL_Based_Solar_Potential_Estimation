from pathlib import Path

import rasterio
from rasterio.windows import Window


def tile_raster(input_path, output_dir, size=256):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with rasterio.open(input_path) as source:
        for row in range(0, source.height - size + 1, size):
            for col in range(0, source.width - size + 1, size):
                window = Window(col, row, size, size)
                profile = source.profile.copy()
                profile.update(height=size, width=size, transform=source.window_transform(window))
                path = output_dir / f"{Path(input_path).stem}_{row}_{col}.tif"
                with rasterio.open(path, "w", **profile) as target:
                    target.write(source.read(window=window))
