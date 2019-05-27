#Classifying images of clothing
from __future__ import absolute_imports, division, print_function, unicode_literals

#Import Tensorflow and Tensorflow datasets
import tensorflow as tf
import tensorflow_datasets as tfds
tf.logging.set_versobility(tf.logging.ERROR)

#Helper libraries
import math
import numpy as np
import matpotlib.pyplot as plt

#Improve bar progress display
import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm

print(.tf__version__)