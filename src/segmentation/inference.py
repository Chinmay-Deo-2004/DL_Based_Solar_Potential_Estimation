from pathlib import Path

import numpy as np
import rasterio
import tensorflow as tf


def predict_mask(model_path, image_path, output_path, threshold=0.5):
    with rasterio.open(image_path) as source:
        image = source.read([1, 2, 3]).transpose(1, 2, 0).astype(np.float32) / 255.0
        profile = source.profile.copy()
    model = tf.keras.models.load_model(model_path, compile=False)
    mask = (model.predict(image[None], verbose=0)[0, ..., 0] >= threshold).astype("uint8")
    profile.update(count=1, dtype="uint8")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(output_path, "w", **profile) as target:
        target.write(mask, 1)
    return mask
