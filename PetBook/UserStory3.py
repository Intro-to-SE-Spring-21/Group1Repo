# User Story 3 (User Activities)

import os
from flask import Flask, render_template, url_for, redirect
from flask import request, session

app = Flask(__name__)

# Insert comment function
@app.route('/comment', methods = ['GET', 'POST'])
def comment():

    if __name__ == '__main__':
        app.run()
