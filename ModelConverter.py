import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(Users/weeyw/Desktop/face-mask-detector/mask_detector.model)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)