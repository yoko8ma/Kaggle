import keras

model = keras.models.load_model('model.h5')
print(model.summary())

