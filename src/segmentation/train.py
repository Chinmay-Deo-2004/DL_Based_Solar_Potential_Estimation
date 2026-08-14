import argparse
from pathlib import Path

import tensorflow as tf

from models import build_unet, build_unetpp
from preprocessing.dataset import load_pairs


def dice(y_true, y_pred):
    y_true = tf.keras.backend.flatten(y_true)
    y_pred = tf.keras.backend.flatten(y_pred)
    return (2 * tf.keras.backend.sum(y_true * y_pred) + 1) / (tf.keras.backend.sum(y_true) + tf.keras.backend.sum(y_pred) + 1)


def loss(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.binary_crossentropy(y_true, y_pred)) + 1 - dice(y_true, y_pred)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--model", choices=("unet", "unetpp"), default="unet")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    x_train, y_train = load_pairs(args.data_dir / "train", args.data_dir / "train_labels")
    x_val, y_val = load_pairs(args.data_dir / "val", args.data_dir / "val_labels")
    model = build_unet() if args.model == "unet" else build_unetpp()
    model.compile(optimizer="adam", loss=loss, metrics=["accuracy", dice, tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
    callbacks = [
        tf.keras.callbacks.ReduceLROnPlateau(patience=3, factor=0.5),
        tf.keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True),
    ]
    model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=args.epochs, batch_size=args.batch_size, callbacks=callbacks)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    model.save(args.output)


if __name__ == "__main__":
    main()
