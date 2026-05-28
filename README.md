# Cancer Mortality Prediction Across US Counties

Cancer death rates in the US vary a lot by county; sometimes by a factor of two or three between neighboring regions. Some of that variation is explained by incidence rates, but a surprising amount comes down to socioeconomic factors: how poor a county is, how many people are uninsured, how isolated the population is.

This project tries to model that relationship. I merged county-level cancer data from the CDC with the Social Vulnerability Index, trained an XGBoost model to predict mortality rates, and used SHAP to figure out which features actually matter.

---

## Project Structure

```
us-county-cancer-mortality-ml/
├── data/                     # not tracked in git (see below)
├── notebooks/
│   └── 01_cancer_mortality_prediction.ipynb
├── visualizations/
│   ├── actual_vs_predicted.png
│   ├── cancer_mortality_map.html
│   ├── shap_beeswarm.png
│   └── shap_feature_importance.png
├── main.py
├── requirements.txt
└── README.md
```

---

## Data

Three datasets, all publicly available:

- Cancer incidence by county - NCI SEER
- Cancer mortality by county, 2019–2023 — CDC Wonder
- Social Vulnerability Index, 2022 — CDC ATSDR

They were joined on FIPS county codes. Counties with suppressed mortality counts (typically rural areas with small populations) were dropped rather than imputed, since the uncertainty there would have been too high.

---

## Approach

The target is the age-adjusted cancer mortality rate per 100,000. Features include cancer incidence rates and about 15 SVI variables covering poverty, insurance coverage, housing, and minority status.

I went with XGBoost mostly because it handles skewed distributions and missing values reasonably well without a lot of preprocessing. After tuning with cross-validation, I ran SHAP to get a clearer picture of what the model was actually picking up on — feature importance scores from tree models can be misleading on their own.

---

## Results

The R² on the test set came out around 0.75. The strongest predictors were cancer incidence rate, poverty rate, and the share of residents without health insurance — which lines up with what the public health literature says about late-stage diagnosis rates in underserved counties.

### Actual vs. Predicted

![Actual vs Predicted](visualizations/actual_vs_predicted.png)

### SHAP Feature Importance

![SHAP Feature Importance](visualizations/shap_feature_importance.png)

### SHAP Beeswarm

![SHAP Beeswarm](visualizations/shap_beeswarm.png)

The interactive map (`visualizations/cancer_mortality_map.html`) shows predicted mortality across all counties and makes the geographic clustering pretty clear — open it in a browser.

---

## Running it

```bash
git clone https://github.com/johnbozorgi/us-county-cancer-mortality-ml.git
cd us-county-cancer-mortality-ml
```

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python main.py
```

The data files aren't included in the repo because they're too large. Download links are in the notebook.

---

## Dependencies

`xgboost` · `shap` · `scikit-learn` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `plotly`

---

## Author

**Hamid Janbozorgi**

MS Computer Science — University of Illinois Urbana-Champaign (UIUC)

[hamidj2@illinois.edu](mailto:hamidj2@illinois.edu) · [github.com/johnbozorgi](https://github.com/johnbozorgi)
