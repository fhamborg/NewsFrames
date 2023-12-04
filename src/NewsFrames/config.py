from pathlib import Path

AFF = "AFF"
CULT = "CULT"
ECON = "ECON"
GOV = "GOV"

WITHOUT_ATTRIBUTES = "withoutattributes"
WITH_ATTRIBUTES = "withattributes"

DIMENSIONS = (AFF, CULT, ECON, GOV)

BASE_PATH = Path(".")
DATA_PATH = BASE_PATH / "data"


DIM2MODEL_PATH = {
    # with 3 attributes plus NOT if dimension is not present
    (AFF, WITH_ATTRIBUTES): "fhamborg/newsframes-aff",
    (CULT, WITH_ATTRIBUTES): "fhamborg/newsframes-cult",
    (ECON, WITH_ATTRIBUTES): "fhamborg/newsframes-econ",
    (GOV, WITH_ATTRIBUTES): "fhamborg/newsframes-gov",
    # without attributes, i.e., only whether dimension is present or not
    (AFF, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-aff-bin",
    (CULT, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-cult-bin",
    (ECON, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-econ-bin",
    (GOV, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-gov-bin",
}
