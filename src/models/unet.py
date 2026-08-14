from tensorflow.keras import Model, layers


def _block(x, filters, name):
    x = layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_1")(x)
    return layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_2")(x)


def build_unet(input_shape=(256, 256, 3)):
    inputs = layers.Input(input_shape)
    c1 = _block(inputs, 64, "encoder_1"); p1 = layers.MaxPooling2D()(c1)
    c2 = _block(p1, 128, "encoder_2"); p2 = layers.MaxPooling2D()(c2)
    c3 = _block(p2, 256, "encoder_3"); p3 = layers.MaxPooling2D()(c3)
    b = _block(p3, 512, "bottleneck")
    d3 = _block(layers.Concatenate()([layers.Conv2DTranspose(256, 2, 2)(b), c3]), 256, "decoder_3")
    d2 = _block(layers.Concatenate()([layers.Conv2DTranspose(128, 2, 2)(d3), c2]), 128, "decoder_2")
    d1 = _block(layers.Concatenate()([layers.Conv2DTranspose(64, 2, 2)(d2), c1]), 64, "decoder_1")
    return Model(inputs, layers.Conv2D(1, 1, activation="sigmoid")(d1), name="unet")
