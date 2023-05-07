import tensorflow as tf
import numpy as np

# Define the pre-trained model path
model_path = 'path/to/pretrained/model'

# Define the class labels
class_labels = ['Bacterial_spot', 'Early_blight', 'Late_blight', 'Leaf_mold', 'Septoria_leaf_spot', 'Spider_mites', 'Target_spot', 'Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_mosaic_virus', 'healthy']

# Load the pre-trained model
model = tf.keras.models.load_model(model_1)

# Define the image size
img_size = 224

# Define a function to preprocess the input image
def preprocess_img(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(img_size, img_size))
    img_arr = tf.keras.preprocessing.image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    img_arr /= 255.
    return img_arr

# Define a function to predict the class of the input image
def pred_tomato_disease(tomato_plant):
    # Preprocess the input image
    img_arr = preprocess_img(tomato_plant)
    
    # Make the prediction
    pred = model.predict(img_arr)
    
    # Get the class label with highest probability
    pred_class = class_labels[np.argmax(pred)]
    
    # Set the output page based on the predicted class
    if pred==0:
      return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
       
    elif pred==1:
      return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'
        
    elif pred==2:
      return "Tomato - Late Blight Disease", 'Tomato - Late_blight.html'
       
    elif pred==3:
      return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
        
    elif pred==4:
      return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
        
    elif pred==5:
      return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'
    
    elif pred==6:
      return "Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'
        
    elif pred==7:
     return "Tomato - Tomoato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'

    elif pred==8:
       return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
    
    elif pred==9:
      return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'
    
    return pred_class, output_page
