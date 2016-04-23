from flask import Flask, request, url_for, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()
data = [{'id':1,'nama_produk':'sepatu1','deskripsi_produk':'merupakan jenis tas1','harga':'100.00'}, {'id':2,'nama_produk':'sepatu2','deskripsi_produk':'merupakan jenis tas2','harga':'200.00'}]
data2 = [{'id':1,'nama_konsumen':'konsumen1','username':'username1','password':'password1'}, {'id':2,'nama_konsumen':'konsumen2','username':'username2','password':'password2'}]
data3 = [{'id':1,'tangal':'tanggal1','pembelian':'pembelian1'}, {'id':2,'tangal':'tanggal2','pembelian':'pembelian2'}]

def make_public_url(member):
	new_member = {}
	for field in member:
		if field == 'id':
			new_member['uri'] = url_for('id_by_produk', id=member['id'], _external=True)
		else:
			new_member[field] = member[field]
	return new_member

@auth.get_password
def get_pw(username):
	for member in data2:
		if str(member['username']) == username:
			return str(member['password'])
	return None

@auth.error_handler
def auth_error():
	return make_response(jsonify({'error':'Unauthorized access'}), 401)


#=============================================================
#perintah 1
@app.route("/produk", methods=['GET','POST','DELETE'])
def produk():
	if request.method == 'GET':
		return jsonify({'data':[make_public_url(member) for member in data]})
	return '''
	<html>
	'''

	if request.method == 'POST':
		newid = request.form['id']
		newnamaproduk = request.form['nama_produk']
		newdeskripsiproduk = request.form['deskripsi_produk']
		newharga = request.form['harga']
		for member in data :
			if str(member['id']) == newid :
				return json.dumps({'error : duplicate data'})
		data.append({'id':newid,'nama produk':newnamaproduk,'deskripsi produk':newdeskripsiproduk,'harga':newharga})
		return json.dumps({'succes : data inserted'})	

	if request.method == 'DELETE':
		for member in data :
			if str(member['id']) == id :
				data.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})

#=============================================================
@app.route("/produk/<id>", methods=['GET','DELETE','PUT'])
def id_by_produk(id):
	if request.method == 'GET':
		for member in data:
			if str(member['id']) == id:
				return json.dumps(member)
		return json.dumps({'error':'data not found'})

	if request.method == 'DELETE':
		for member in data :
			if str(member['id']) == id :
				data.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})

	if request.method == 'PUT':
		for member in data :
			if str(member['id']) == id :
				member['nama_produk'] = request.form['nama_produk']
				member['deskripsi_produk'] = request.form['deskripsi_produk']
				member['harga'] = request.form['harga']
			return json.dumps({'sucess':'data '+id +' has been modified'})
		return json.dumps({'error':'data not found'})

#=============================================================
#perintah 2
@app.route("/konsumen", methods=['GET','POST','DELETE'])
def konsumen():
	if request.method == 'GET':
		return json.dumps(data2)

	if request.method == 'POST':
		newid = request.form['id']
		newnamakonsumen = request.form['nama_konsumen']
		newusernamekonsumen = request.form['username']
		newpasswordkonsumen = request.form['password']
		for member in data2 :
			if str(member['id']) == newid :
				return json.dumps({'error : duplicate data'})
		data2.append({'id':newid,'nama konsumen':newnamakonsumen,'username':newusernamekonsumen,'password':newpasswordkonsumen})
		return json.dumps({'succes : data inserted'})

	if request.method == 'DELETE':
		for member in data2 :
			if str(member['id']) == id :
				data2.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})

#=============================================================
@app.route("/konsumen/<id>", methods=['GET','DELETE','PUT'])
@auth.login_required
def id_by_konsumen(id):
	if request.method == 'GET':
		for member in data2:
			if str(member['id']) == id:
				return json.dumps(member)
		return json.dumps({'error':'data not found'})

	if request.method == 'DELETE':
		for member in data2:
			if str(member['id']) == id :
				data2.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})

	if request.method == 'PUT':
		for member in data2 :
			if str(member['id']) == id :
				newnamakonsumen = request.form['nama_konsumen']
				newusernamekonsumen = request.form['username']
				newpasswordkonsumen = request.form['password']
			return json.dumps({'sucess':'data '+id +' has been modified'})
		return json.dumps({'error':'data not found'})

#=============================================================
#perintah 3
@app.route("/riwayat", methods=['GET','POST','DELETE'])
@auth.login_required
def riwayat():
	if request.method == 'GET':
		return json.dumps(data3)

	if request.method == 'POST':
		newid = request.form['id']
		newtanggal = request.form['tanggal']
		newpembelian = request.form['pembelian']
		for member in data3 :
			if str(member['id']) == newid :
				return json.dumps({'error : duplicate data'})
		data3.append({'id':newid,'tanggal':newtanggal,'pembelian':newpembeian})
		return json.dumps({'succes : data inserted'})

	if request.method == 'DELETE':
		for member in data3 :
			if str(member['id']) == id :
				data3.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})

#=============================================================
@app.route("/riwayat/<id>", methods=['GET','DELETE'])
@auth.login_required
def id_by_riwayat(id):
	if request.method == 'GET':
		for member in data2:
			if str(member['id']) == id:
				return json.dumps(member)
		return json.dumps({'error':'data not found'})

	if request.method == 'DELETE':
		for member in data2:
			if str(member['id']) == id :
				data2.remove(member)
			return json.dumps({'sucess':'data '+id +' deleted'})
		return json.dumps({'error':'data not found'})


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
