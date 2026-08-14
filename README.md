# Solar Potential Estimation

Code accompanying *Comparative Analysis of U-Net and U-Net++ for Rooftop Segmentation in Solar Potential Estimation*.

The project segments rooftops from satellite imagery and estimates annual solar potential from the predicted rooftop area and clear-sky irradiance.

## Project structure

```text
src/
  models/          U-Net and U-Net++
  preprocessing/   GeoTIFF tiling and dataset loading
  segmentation/    Training, evaluation, and inference
  geospatial/      Polygon and area utilities
  solar/           Irradiance and energy calculations
notebooks/         Experiment notebooks
app/               Streamlit application
models/            Model checkpoints (not committed)
examples/          Example inputs and outputs
results/           Figures and solar maps (not committed)
```

## Setup

```bash
git clone https://github.com/<username>/solar-potential-estimation.git
cd solar-potential-estimation
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Data layout

```text
data/
  train/          train_labels/
  val/            val_labels/
  test/           test_labels/
```

Images must be RGB GeoTIFFs and masks must be single-band TIFFs. Building pixels are encoded as 255 and background as 0. The dataset is not included in this repository.

## Train

```bash
PYTHONPATH=src python -m segmentation.train --data-dir data --model unet --output models/unet/model.keras
PYTHONPATH=src python -m segmentation.train --data-dir data --model unetpp --output models/unetpp/model.keras
```

## Results reported in the paper

| Metric | U-Net | U-Net++ |
| --- | ---: | ---: |
| Accuracy | 0.9325 | 0.9351 |
| Dice | 0.7613 | 0.8094 |
| F1 | 0.8040 | 0.8094 |
| IoU | 0.6277 | 0.6839 |
| Precision | 0.8009 | 0.8218 |
| Recall | 0.8304 | 0.8164 |

## Citation

```bibtex
@inproceedings{deo2025rooftop,
  title={Comparative Analysis of U-Net and U-Net++ for Rooftop Segmentation in Solar Potential Estimation},
  author={Deo, Chinmay and Singh, Manjeet},
  booktitle={2025 IEEE International Conference on Intelligent Signal Processing and Effective Communication Technologies (INSPECT)},
  year={2025},
  doi={10.1109/INSPECT67393.2025.11350341}
}
```
