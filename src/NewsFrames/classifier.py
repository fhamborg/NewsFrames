from collections import defaultdict
from typing import List, Iterable, Union

from loguru import logger
from setfit import SetFitModel

from .config import (
    DIMENSIONS,
    DIM2MODEL_PATH,
    WITH_ATTRIBUTES,
    WITHOUT_ATTRIBUTES,
    DIM2ID2LABEL,
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

        # restructure predictions to have all predictions for one sentence in one list
        sentenceindex2predictions_raw = defaultdict(list)
        for dimension, predictions in dim2predictions.items():
            for index, prediction in enumerate(predictions):
                sentenceindex2predictions_raw[index].append(prediction)

        # add some convenience info
        sentenceindex2predictions = {}
        for sentenceindex, predictions in sentenceindex2predictions_raw.items():
            assert len(predictions) == len(self.dimensions)

            labels = []
            for dimension, label_id in zip(self.dimensions, predictions):
                label = self.get_label(dimension, label_id)
                labels.append(label)

            sentenceindex2predictions[sentenceindex] = {
                "label_ids": tuple(predictions),
                "labels": tuple(labels),
            }

        return {
            "predicted_dimensions": self.dimensions,
            "attribute_mode": self.attribute_mode,
            "sentenceindex_to_predictions": sentenceindex2predictions,
            "dimension_to_predictions": dim2predictions,
            "sentences": sentences,
        }

    def get_label(self, dimension: str, label_id: int):
        assert dimension in self.dimensions
        return DIM2ID2LABEL[(dimension, self.attribute_mode)][label_id]
