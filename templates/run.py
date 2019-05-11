from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update({
	'DEBUG':True,
	'SECRET_KEY':'my funny secret key here',
	'SQLALCHEMY_DATABASE_URI':'sqlite:////breast.db',
	})

# instantiate database object
db = SQLAlchemy(app)

############################# MODELS ###################################

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)


############################# ROUTES ###################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account')
def create_account():
	return ''

@app.route('/patient')
def patient():
	'''
	 Patient submits image, system detects the image and process
	 image must be of breast return invalid image if otherwise
	 If required image, the results should be positive or negative
	 depending i the patient has cancer

	 Create a counter variable to track all registered users and statistics

	'''
	return ''



if __name__ == '__main__':
    app.run()
