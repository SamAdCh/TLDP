#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'www.kaggleusercontent.com/kf/69052527/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..ujLWeLI3GupETjqVbfpHSQ.wywZsBXieb94kHBkzgScTwPD95s3ZKxU-q0EuCbY7-U5j1zUN-zIWWfPUfsBuLsqsa2TRzQ4J-eMXdOKf9QgrZDNPNwkeXkIf3JK8z--ERvc4XRkw8VVEsBfqLJgdXsGgXqKIVodPbp79Pbc-AWWPp05rE4vubZ7EaIuuPCvRqI0M6TXVmLl3Pg2PHlPZjMiGHBkF7pTWvuzHQUTxUF0o0dpQMUgrB99yEuoFQ_PxN6UCDoXRG7xZNgrvFKGXKmbbJ_nBbW9-AP0gMzJKNa4WlXnhCnqgTeOSH2QMl_8s_wbGWOdwOcz21IrCGeRIA26J4YMIw96d49uveWoLA9HhH4DUJ_G25ovkwA9jfAyop2R0YM0kD1omeQE7Qgcxzyl7MGSgHWhRiXiwEJGU2P1SqRUfh61eU5wENoW5NSRRfl_E-159WQ4XJynmlrYD_38oBXwi0AFqpjNFDn7GCvYuP8DOEjZ9okPnPPAbrid3B0Jc38_-QWhBNOdYaCsOKYvITq5he1ip6kuawws16Ur98RTDK-VMURhOaxai6b2mXkc0sTv7FloBDHYbuQvUu13plYzs-RkUi552GGrdsmlV8imwIxOgLkSDvAHageU2Z8Zy9Wrx-QwHnwkHq_VXuIt6xzt7pcvn348RYiAofOHrZOCXqwF8y7QulW-lz1qKDs9dWkGgLnd4IaWYvgiu8ktYlxjhyBzw7LDEo2KIxIE8w.bH1GlhGF1OBPmvpez6sEPQ/InceptionV3_256.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
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
    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=1010)

    import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM my_table")

# Fetch results
results = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
conn.close()
    
    
