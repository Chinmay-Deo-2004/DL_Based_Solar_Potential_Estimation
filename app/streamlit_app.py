from pathlib import Path
from tempfile import TemporaryDirectory

import streamlit as st

from segmentation.inference import predict_mask


st.set_page_config(page_title="Solar Potential Estimation")
st.title("Solar Potential Estimation")

model_path = st.text_input("Model path", "models/unet/model.keras")
image = st.file_uploader("GeoTIFF image", type=("tif", "tiff"))

if image and st.button("Segment rooftops"):
    if not Path(model_path).exists():
        st.error("Model file not found.")
    else:
        with TemporaryDirectory() as directory:
            input_path = Path(directory) / image.name
            output_path = Path(directory) / "mask.tif"
            input_path.write_bytes(image.getvalue())
            mask = predict_mask(model_path, input_path, output_path)
            st.image(mask * 255, caption="Rooftop mask")
            st.download_button("Download mask", output_path.read_bytes(), "rooftop_mask.tif", "image/tiff")
