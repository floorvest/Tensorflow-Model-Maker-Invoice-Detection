import numpy as np
import os

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)


spec = model_spec.get('efficientdet_lite0')

label = ["invoice_title", "invoice_table", 'invoice_total']

train_data = object_detector.DataLoader.from_pascal_voc(images_dir='data/images/train', annotations_dir='data/images/train', label_map=label)
test_data = object_detector.DataLoader.from_pascal_voc(images_dir='data/images/test', annotations_dir='data/images/test', label_map=label)

model = object_detector.create(train_data, model_spec=spec, epochs=50, batch_size=8, train_whole_model=True, validation_data=test_data)

model.evaluate(test_data)

model.export(export_dir='.')

model.evaluate_tflite('model.tflite', test_data)
