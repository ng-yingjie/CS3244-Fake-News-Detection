import tensorflow as tf
import autokeras as ak
# from keras.models import model_from_json

with open('my_model.json', 'r') as json_file:
    json_string= json_file.read()

# model = model_from_json(json_string)
model = tf.keras.models.model_from_json(json_string, custom_objects=ak.CUSTOM_OBJECTS)

# print(model.summary())
print(model.layers)
