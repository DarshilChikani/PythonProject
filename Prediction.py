img = image.load_img(r'C:\NewDrive\0PG College\Python 2\Project data\color_val\Blueberry___healthy\0a3f8b2f-9bb1-4da9-85a1-fb5a52c059e2___RS_HL 2478.JPG',target_size=(224,224))
img = image.img_to_array(img)
img=np.expand_dims(img,axis=0)
predictedclass = loaded_model.predict(img)
#print(predictedclass)

#print(train_generator.class_indices)

for i in train_generator.class_indices:
    if train_generator.class_indices[i] == np.argmax(predictedclass):
        print(i)
        break