from typing import List, Iterable, Union

from loguru import logger
from setfit import SetFitModel

from src.NewsFrames.config import (
    DIMENSIONS,
    DIM2MODEL_PATH,
    WITH_ATTRIBUTES,
    WITHOUT_ATTRIBUTES,
)


class Classifier:
    def __init__(
        self, dimensions: List[str] = DIMENSIONS, attribute_mode: str = WITH_ATTRIBUTES
    ):
        logger.debug("Creating classifier with dimensions {}", dimensions)
        for dimension in dimensions:
            assert dimension in DIMENSIONS, f"Dimension {dimension} not in {DIMENSIONS}"
        assert attribute_mode in (WITH_ATTRIBUTES, WITHOUT_ATTRIBUTES)
        self.dimensions = dimensions
        self.attribute_mode = attribute_mode
        self.dim2model = self.load_models()

        logger.info("Created classifier with dimensions {}", self.dimensions)

    def load_models(self):
        dim2model = {}
        for dimension in self.dimensions:
            model_path = DIM2MODEL_PATH[(dimension, self.attribute_mode)]
            logger.debug("Loading model for {} from {}", dimension, model_path)
            model = SetFitModel.from_pretrained(model_path)
            dim2model[dimension] = model
            logger.debug("Loaded model for {} from {}", dimension, model_path)

        return dim2model

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

        dim2predictions = {}
        for dimension, model in self.dim2model.items():
            logger.debug(
                "Predicting for dimension {} (num predictions = {})",
                dimension,
                len(sentences),
            )
            predictions = model.predict(sentences)
            assert predictions.shape == (len(sentences),)
            predictions = predictions.tolist()

            dim2predictions[dimension] = predictions
            logger.debug("Predictions for dimension {}: {}", dimension, predictions)

        return dim2predictions


def main():
    classifier = Classifier()
    print(classifier.predict(["conserve the environment", "power to the people!"]))


if __name__ == "__main__":
    main()
