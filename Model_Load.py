from keras.models import model_from_json

# Saved Model again loaded and compiled to run

json_file = open(r'C:\Users\Darshil Chikani\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(r"C:\Users\Darshil Chikani\model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(optimizer=SGD(lr=1e-4,decay=1e-6, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])