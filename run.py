from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.update({
	'DEBUG':True,
	'SECRET_KEY':'my funny secret key here',
	'SQLALCHEMY_DATABASE_URI':'sqlite:////breast.db',
	})

# instantiate database object
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

############################# MODELS ###################################

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    age = db.Column('age',db.String(30))
    name = db.Column('name', db.String(20), index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    date_joined = db.Column('date_joined' , db.DateTime)
 
    def __init__(self , name ,password , email, age):
        self.name = name
        self.password = password
        self.email = email
        self.age = age
        self.date_joined = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)


############################ UTILITY FUNCTIONS #########################

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



############################# ROUTES ###################################

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
	    return render_template('index.html')
	email = request.form['email']
	password = request.form['password']
	# get the email and password variable from the form
	return redirect(url_for('patient'))

@app.route('/create_account')
def create_account():
	return ''

@app.route('/patient', methods=['GET', 'POST'])
def patient():
	'''
	 Patient submits image, system detects the image and process
	 image must be of breast return invalid image if otherwise
	 If required image, the results should be positive or negative
	 depending i the patient has cancer

	 Create a counter variable to track all registered users and statistics

	'''
	if request.method == 'GET':
	    return render_template('patient.html')



if __name__ == '__main__':
    app.run()
