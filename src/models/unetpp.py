from tensorflow.keras import Model, layers


def _block(x, filters, name):
    x = layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_1")(x)
    return layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_2")(x)


def build_unetpp(input_shape=(256, 256, 3)):
    inputs = layers.Input(input_shape)
    x00 = _block(inputs, 64, "x00")
    x10 = _block(layers.MaxPooling2D()(x00), 128, "x10")
    x20 = _block(layers.MaxPooling2D()(x10), 256, "x20")
    x01 = _block(layers.Concatenate()([x00, layers.UpSampling2D()(x10)]), 64, "x01")
    x11 = _block(layers.Concatenate()([x10, layers.UpSampling2D()(x20)]), 128, "x11")
    x02 = _block(layers.Concatenate()([x00, x01, layers.UpSampling2D()(x11)]), 64, "x02")
    return Model(inputs, layers.Conv2D(1, 1, activation="sigmoid")(x02), name="unetpp")
