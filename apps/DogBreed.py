import logging
import tensorflow as tf

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DogBreed(object):
    """Class DogBreed"""

    def __init__(self, models_dir="/models/dog_model/1"):
        self.loaded = False
        logging.info("Load model here...")
        self._models_dir = models_dir

    def load(self):
        self._dog_model = tf.keras.models.load_model(f"{self._models_dir}")
        self.loaded = True
        logging.info("Model has been loaded and initialized...")

    def predict(self, X, feature_names=None):
        """Predict Method"""
        if not self.loaded:
            logging.info("Not loaded yet.")
            self.load()
        logging.info("Model loaded.")
        probs = self._dog_model.predict(X)
        return probs
