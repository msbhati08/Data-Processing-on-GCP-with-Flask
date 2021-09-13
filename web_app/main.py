from flask import Flask, render_template, render_template_string
from google.cloud import storage

app = Flask(__name__)

# Initialize variables
BUCKET_NAME = 'webpage-static-content-bucket'

# Initialize the bucket you created containing the templates
bucket = storage.Client().bucket(BUCKET_NAME)

@app.route('/')
def index():
    # render_template to render the homepage
    return render_template('index.html')

@app.route('/csv')
def show_csv():
    # Load the template string from Cloud Storage
    template_string = bucket.blob('output_csv.html').download_as_string().decode('utf-8')

    # Using render_template_string to render csv file from bucket
    return render_template_string(template_string, name='CSV')

@app.route('/prn')
def show_prn():
    # Load the template string from Cloud Storage
    template_string = bucket.blob('output_prn.html').download_as_string().decode('utf-8')

    # Using render_template_string to render prn file from bucket
    return render_template_string(template_string, name='PRN')

@app.errorhandler(500)
def server_error(e):
    # Log the error
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500