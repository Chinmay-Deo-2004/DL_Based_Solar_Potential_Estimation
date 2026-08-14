# Methodology

1. Clean image-mask pairs from the Massachusetts Buildings Dataset.
2. Split imagery into train, validation, and test sets.
3. Tile 1500×1500 imagery into non-overlapping 256×256 patches.
4. Train U-Net and U-Net++ with Adam and BCE + Dice loss.
5. Compare Dice, IoU, F1, precision, recall, accuracy, and loss.
6. Run inference on georeferenced imagery.
7. Polygonize predicted rooftop masks and calculate rooftop area in a projected CRS.
8. Calculate clear-sky annual POA irradiance with pvlib.
9. Estimate annual energy: `area × irradiation × efficiency`.

The paper used a batch size of 16, `ReduceLROnPlateau(patience=3, factor=0.5)`, and `EarlyStopping(patience=6, restore_best_weights=True)`.
