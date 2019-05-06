#NOTE: This will not work in windows, run in Google Colab if you do not have access to a linux machine.
from tensorflow.contrib import lite
converter = lite.TFLiteConverter.from_keras_model_file( 'model.h5' )
model = converter.convert()
file = open( 'model.tflite' , 'wb' )
file.write( model )
