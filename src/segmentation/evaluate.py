import argparse
from pathlib import Path

import tensorflow as tf

from preprocessing.dataset import load_pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    args = parser.parse_args()
    x_test, y_test = load_pairs(args.data_dir / "test", args.data_dir / "test_labels")
    model = tf.keras.models.load_model(args.model, compile=False)
    results = model.evaluate(x_test, y_test, return_dict=True)
    for name, value in results.items():
        print(f"{name}: {value:.4f}")


if __name__ == "__main__":
    main()
