from pathlib import Path

import numpy as np
import rasterio


def _read_image(path):
    with rasterio.open(path) as source:
        return source.read([1, 2, 3]).transpose(1, 2, 0).astype(np.float32) / 255.0


def _read_mask(path):
    with rasterio.open(path) as source:
        return (source.read(1) > 0).astype(np.float32)[..., None]


def load_pairs(image_dir, mask_dir):
    images = sorted(Path(image_dir).glob("*.tif*"))
    masks = sorted(Path(mask_dir).glob("*.tif*"))
    if not images or len(images) != len(masks):
        raise ValueError("Image and mask directories must contain equal non-empty TIFF collections.")
    return np.stack([_read_image(path) for path in images]), np.stack([_read_mask(path) for path in masks])
