"""
Routes and views for the flask application.
"""

#imports
import os
from flask import request, redirect
from flask import Flask,  render_template
from Usrstory2 import app
from werkzeug.utils import secure_filename

app =Flask(__name__)

#allows what files are used
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

#save folder/upload to DB
app.config["UPLOAD_IMAGE"] = r"C:\Users\Andrew Wells\Desktop"


# upload image function 
@app.route('/upload',  methods= ['GET', 'POST'])
def upload():
    #request images
    if request.method == 'POST':

        if request.files:

            img = request.files["Image"]

            img.save(os.path.join(app.config["UPLOAD_IMAGE"], img.filename))

            return redirect(url_for('upload'))

            return render_template('/upload.html')

    if __name__ == '__main__':
        app.run(debug=True)




         