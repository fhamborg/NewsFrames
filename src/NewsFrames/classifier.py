from typing import List, Iterable, Union

from loguru import logger


class Classifier:
    AFF = "AFF"
    CULT = "CULT"
    ECON = "ECON"
    GOV = "GOV"

    DIMENSIONS = (AFF, CULT, ECON, GOV)

    def __init__(self, dimensions: List[str] = DIMENSIONS):
        for dimension in dimensions:
            assert (
                dimension in Classifier.DIMENSIONS
            ), f"Dimension {dimension} not in {Classifier.DIMENSIONS}"
        self.dimensions = dimensions
        self.dim2model = self.load_models()

        logger.info("Created classifier with dimensions {}", self.dimensions)

    def load_models(self):
        return {}

    def predict(self, sentences: Union[Iterable[str], str]):
        """

        :param sentences:
        :return:
        """
        if isinstance(sentences, str):
            sentences = [sentences]
        for i, sentence in enumerate(sentences):
            assert isinstance(
                sentence, str
            ), f"Expected sentences to be str, got {type(sentence)} for {i}-th item"

        return ["hi"] * len(sentences)


