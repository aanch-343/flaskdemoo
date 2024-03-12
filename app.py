from flask import Flask, request
import os
import base64

application = Flask(__name__)

@application.route('/receive-image', methods=['POST'])
def receive_image():
    data = request.get_json()
    image = data['image']
    imageName = data['imageName']
    question = data['question']
    answerkey = data['answerkey']

    # Convert base64 string to bytes
    image_bytes = base64.b64decode(image)

    # Save the image to disk
    image_path = os.path.join('/tmp', imageName)
    with open(image_path, 'wb') as f:
        f.write(image_bytes)

    # Log the received data
    print("Received Data:")
    print("Question:", question)
    print("Answer Key:", answerkey)
    print("Image saved as:", image_path)

    return {'message': 'Data received successfully'}
