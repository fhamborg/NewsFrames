from typing import List

from loguru import logger


class Classifier:
    AFF = "AFF"
    CULT = "CULT"
    ECON = "ECON"
    GOV = "GOV"

    DIMENSIONS = [AFF, CULT, ECON, GOV]

    def __init__(self, dimensions: List[str] = None):
        for dimension in dimensions:
            assert (
                dimension in Classifier.DIMENSIONS
            ), f"Dimension {dimension} not in {Classifier.DIMENSIONS}"
        self.dimensions = dimensions
        self.dim2model = self.load_models()

        logger.info("Created classifier with dimensions {}", self.dimensions)

    def predict(self, sentences: List[str]):
        """

        :param sentences:
        :return:
        """
        return ["hi"] * len(sentences)
