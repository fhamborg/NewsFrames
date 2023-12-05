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

DIM2ID2LABEL = {
    (AFF, WITH_ATTRIBUTES): {
        0: "AFF_NEG",
        1: "AFF_NOT",
        2: "AFF_POS",
        3: "AFF_RAT",
    },
    (CULT, WITH_ATTRIBUTES): {
        0: "CULT_GAL",
        1: "CULT_NEU",
        2: "CULT_NOT",
        3: "CULT_TAN",
    },
    (ECON, WITH_ATTRIBUTES): {
        0: "ECON_LEFT",
        1: "ECON_NEU",
        2: "ECON_NOT",
        3: "ECON_RIGHT",
    },
    (GOV, WITH_ATTRIBUTES): {
        0: "GOV_NOT",
        1: "GOV_PLU",
        2: "GOV_POP",
        3: "GOV_TEC",
    },
    (AFF, WITHOUT_ATTRIBUTES): {
        0: "AFF_no",
        1: "AFF_yes",
    },
    (CULT, WITHOUT_ATTRIBUTES): {
        0: "CULT_no",
        1: "CULT_yes",
    },
    (ECON, WITHOUT_ATTRIBUTES): {
        0: "ECON_no",
        1: "ECON_yes",
    },
    (GOV, WITHOUT_ATTRIBUTES): {
        0: "GOV_no",
        1: "GOV_yes",
    },
}
