from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from scrapper.operations_sheet_scrapper import OperationsSheetFlavor
from service.taxes import TaxCalculator

ALLOWED_EXTENSIONS = set(['xls'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message': 'No file part in the request'})
		resp.status_code = 400
		return resp

	file = request.files.get('file')
	print(file)

	errors = {}
	success = False

	if file and allowed_file(file.filename):
		# filename = secure_filename(file.filename)
		# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		operations_sheet = OperationsSheetFlavor()
		df = operations_sheet.read_xls(file)
		financial_operations = df.apply(operations_sheet.create_financial_op, axis=1)
		total_tax = TaxCalculator.calculate_tax(financial_operations)
		resp = jsonify(total_tax)
		print (resp)
		success = True
		resp.status_code = 200
		return resp
	else:
		errors['message'] = 'File type is not allowed'
		resp = jsonify(errors)
		resp.status_code = 500
		return resp

if __name__ == "__main__":
    # create the uploads directory if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)