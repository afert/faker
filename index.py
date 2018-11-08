from flask import Flask,request,render_template,url_for
from werkzeug import secure_filename

import dowithimage
from datetime import timedelta

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) 
@app.route('/')
def hello_world():
	return render_template('index.html')
# @app.route('/<username>')
# def show_uername(username):
# 	return 'User is %s'%username

@app.route('/boardingpass')
def boardingpass():
	return render_template('boardingpass.html')

@app.route('/do_boardingpass',methods=['GET','POST'])
def do_boardingpass():
	if request.method=='POST':
		name=request.form['name'].upper()
		flight=request.form['flight'].upper()
		flightDate=request.form['date'].upper()
		fromP=request.form['from'].upper()
		toP=request.form['to'].upper()
		dowithimage.doWithBoardingPass(name,flight,flightDate,fromP,toP)
		imgurl=url_for('static',filename='image/boardingpass/sample-out.jpg')
		#imgurl='/static/image/boardingpass/sample-out.jpg'
		return render_template('boardingpass_show.html',imgurl=imgurl)
		#return "The name is %s and filght is %s, Data is %s ,From is %s,To is %s"%(name,flight,flightDate,fromP,toP)
	else:
		return 'something wrong'

@app.route('/trumpsign')
def trumpsign():
	return render_template('trumpsign.html')

@app.route('/do_trumpsign',methods=['GET','POST'])
def do_trumpsign():
	if request.method=='POST':
		page1=request.form['page1']
		page2=request.form['page2']
		dowithimage.doWithTrumpSign(page1,page2)
		imgurl=url_for('static',filename='image/trump/sample-out.jpg')
		
		return render_template('trumpsign_show.html',imgurl=imgurl)		


@app.route('/<int:post_id>')
def show_post(post_id):
	return 'Post is %d'%post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'subpath is %s'%subpath

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		return do_the_login(request.form['username'])
	else:
		return show_the_login_form()
@app.route('/dologin')
def do_the_login(username):
	return 'This is the login function page! You are in '
@app.route('/login_form')
def show_the_login_form():
	return 'This is the FORM PAGE!'


@app.route('/upload',methods=['GET','POST'])
def upload_file():
	if request.method=='POST':
		f=request.files['picfile']
		#f.save(secure_filename(f.filename))
		fname=f.filename
		imgurl=url_for('static',filename=fname)
		f.save(app.root_path+imgurl)
		
		return render_template('upload.html',imgurl=imgurl)
	else:
		return 'The method is GET'




if __name__=='__main__':
	app.run(debug=True)