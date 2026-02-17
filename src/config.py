from pathlib import Path

# Project root = parent of /src
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
DATA_EXTERNAL_DIR = DATA_DIR / "external"
RAW_GUADALQUIVIR_DIR = DATA_RAW_DIR / "GUADALQUIVIR_DATA"


REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

MODELS_DIR = PROJECT_ROOT / "models"

for d in [DATA_RAW_DIR, DATA_PROCESSED_DIR, DATA_EXTERNAL_DIR, FIGURES_DIR, MODELS_DIR]:
    d.mkdir(parents=True, exist_ok=True)
