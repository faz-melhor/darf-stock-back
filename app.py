import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = 'uploads/files/'

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/hello', methods=['GET'])
@cross_origin()
def hello_world():
	return jsonify(hello='world')

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
	# check if the post request has the file part
	if 'files[]' not in request.files:
		resp = jsonify({'message': 'No file part in the request'})
		resp.status_code = 400
		return resp

	files = request.files.getlist('files[]')

	errors = {}
	success = False

	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(errors)
		resp.status_code = 500
		return resp
	if success:
		resp = jsonify(
            {
                'summary': {
                    'positions': [
                        {
                            'stock': 'ITAUSA',
                            'averagePrice': 21.10,
                            'sellingPrice': 10.00,
                            'profitLoss': -11.10
                        },
                        {
                            'stock': 'ITAUSA',
                            'averagePrice': 21.10,
                            'sellingPrice': 30.00,
                            'profitLoss': 8.90
                        }
                    ],
                    'totalPL': -2.2,
                    'tax': 0
                }
            })
		resp.status_code = 201
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 500
		return resp

if __name__ == "__main__":
    # create the uploads directory if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(host='0.0.0.0', debug=True)
