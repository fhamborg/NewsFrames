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
    # with 3 attributes (excluding NOT)
    (AFF, WITH_ATTRIBUTES): "fhamborg/newsframes-aff3",
    (CULT, WITH_ATTRIBUTES): "fhamborg/newsframes-cult3",
    (ECON, WITH_ATTRIBUTES): "fhamborg/newsframes-econ3",
    (GOV, WITH_ATTRIBUTES): "fhamborg/newsframes-gov3",
    # without attributes, i.e., only whether dimension is present or not
    (AFF, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-aff-bin",
    (CULT, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-cult-bin",
    (ECON, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-econ-bin",
    (GOV, WITHOUT_ATTRIBUTES): "fhamborg/newsframes-gov-bin",
}

DIM2ID2LABEL = {
    (AFF, WITH_ATTRIBUTES): {
        0: "AFF_NEG",
        1: "AFF_POS",
        2: "AFF_RAT",
    },
    (CULT, WITH_ATTRIBUTES): {
        0: "CULT_GAL",
        1: "CULT_NEU",
        2: "CULT_TAN",
    },
    (ECON, WITH_ATTRIBUTES): {
        0: "ECON_LEFT",
        1: "ECON_NEU",
        2: "ECON_RIGHT",
    },
    (GOV, WITH_ATTRIBUTES): {
        0: "GOV_PLU",
        1: "GOV_POP",
        2: "GOV_TEC",
    },
    (AFF, WITHOUT_ATTRIBUTES): {
        0: "NO_AFF",
        1: "AFF",
    },
    (CULT, WITHOUT_ATTRIBUTES): {
        0: "NO_CULT",
        1: "CULT",
    },
    (ECON, WITHOUT_ATTRIBUTES): {
        0: "NO_ECON",
        1: "ECON",
    },
    (GOV, WITHOUT_ATTRIBUTES): {
        0: "NO_GOV",
        1: "GOV",
    },
}
