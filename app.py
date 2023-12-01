from flask import Flask, render_template, request, flash, redirect, url_for
import base64
import os
# Import your AI model here

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Set a secret key for security purposes

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.form['image_data']
    if image_data:
        # Decode the image data
        header, encoded = image_data.split(",", 1)
        binary_data = base64.b64decode(encoded)

        # Process the image with your AI model here
        # Save or handle the image as needed
        # ...

        classification_result = '가연성'  # Replace with actual result
        flash('Image successfully uploaded and classified!', 'success')
        return redirect(url_for('index'))
    else:
        return 'No image data received'

if __name__ == '__main__':
    app.run(debug=True)
