import subprocess
import sys

notebooks = [
    "notebooks/01_eda_and_preprocessing.ipynb",
    "notebooks/02_model_training_and_eval.ipynb",
    "notebooks/03_shap_explainability.ipynb",
    "notebooks/04_geospatial_visualization.ipynb",
]

for nb in notebooks:
    print(f"Running {nb}...")
    result = subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", nb, "--inplace"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error in {nb}:\n{result.stderr}")
        sys.exit(1)
    print(f"Done: {nb}")
