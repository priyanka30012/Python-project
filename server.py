from flask import Flask, request, jsonify
from flask_cors import CORS 
import tensorflow as tf
import numpy as np
from io import BytesIO
from keras.preprocessing import image

app = Flask(__name__)
CORS(app)
model_path = "model/my_h5_model.h5"  # Replace with the path to your saved TensorFlow model
model = tf.keras.models.load_model(model_path)


def process_image(image_file):
    img1 = BytesIO(image_file.read())
    # img = img.resize((150, 150)) 
    img = image.load_img(img1, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    print(prediction)
    scientific_number = tf.nn.sigmoid(prediction[0]).numpy()[0]
    
    def scientific_to_percentage(sc_num):
        decimal_num = float(sc_num)
        percentage = decimal_num * 100
        if (percentage < 50):
            percentage = 100 - percentage
        else:
            percentage = percentage
        return percentage

    percentage = scientific_to_percentage(scientific_number)
    percentage_str = '{:.2f}%'.format(percentage)
    if scientific_number > 0.5:
        return "Ai-generated Image: " + percentage_str
    else:
        return "Real Image: " + percentage_str


@app.route('/process_image', methods=['POST'])
def process_image_route():
    # Check if request has image file
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']

    # Process the image
    processed_output = process_image(image)

    return jsonify({'processed_output': processed_output})


if __name__ == '__main__':
    app.run(debug=True, port=3000)