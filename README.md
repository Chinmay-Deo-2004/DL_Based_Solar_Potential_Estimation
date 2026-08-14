<img width="1919" height="1079" alt="Screenshot 2026-08-13 003200" src="https://github.com/user-attachments/assets/4d5b3132-d239-4240-8b7d-c23abf99a869" />

<table>
  <tr>
    <td><b>Models</b></td>
    <td>
      <img src="https://img.shields.io/badge/U--Net-7.70M%20params-4A90E2">
      <img src="https://img.shields.io/badge/U--Net%2B%2B-2.07M%20params-8E44AD">
    </td>
  </tr>

  <tr>
    <td><b>Frameworks</b></td>
    <td>
      <img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow&logoColor=white">
      <img src="https://img.shields.io/badge/pvlib-solar%20modeling-F5A623">
      <img src="https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white">
    </td>
  </tr>

  <tr>
    <td><b>Data</b></td>
    <td>
      <img src="https://img.shields.io/badge/Massachusetts%20Buildings-Dataset-2E86C1">
    </td>
  </tr>

  <tr>
    <td><b>License</b></td>
    <td>
      <img src="https://img.shields.io/badge/License-Apache%202.0-2EA44F?style=flat-square&logo=apache">
    </td>
  </tr>

  <tr>
  <td><b>Publication</b></td>
  <td>
    <a href="https://doi.org/10.1109/INSPECT67393.2025.11350341">
      <img src="https://img.shields.io/badge/DOI-10.1109%2FINSPECT67393.2025.11350341-007EC6">
       <img src="https://img.shields.io/badge/🏆%20Best%20Paper-Signal%20%26%20Image%20Processing-D4A017">
    </a>
  </td>
</tr>
</table>


This project segments rooftops from satellite imagery using deep learning and estimates annual solar potential from the predicted rooftop area and clear-sky irradiance.

## Project structure
```text
.
│
├── src/
│   ├── models/          U-Net and U-Net++ architectures
│   ├── preprocessing/   GeoTIFF tiling and dataset loading
│   ├── segmentation/    Training, evaluation, and inference
│   ├── geospatial/      Polygon extraction and area calculations
│   └── solar/           Irradiance and energy calculations
│
├── notebooks/
│   ├── 01_dataset_preparation.ipynb
│   ├── 02_unet_training.ipynb
│   ├── 03_unetpp_training.ipynb
│   ├── 04_model_comparison.ipynb
│   └── 05_solar_potential_estimation.ipynb
│
├── app/                 Streamlit application
│
├── models/              Pretrained model checkpoints
│   ├── unet.keras
│   └── unetpp.keras
│
├── README.md            Project documentation
├── requirements.txt     Python dependencies
├── LICENSE              Apache License 2.0
└── CITATION.cff         Citation metadata
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

## Results

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

P.S: If you'd like to work further on this project or collaborate on future research, feel free to get in touch at chinmay.deo@telwise-research.com!
