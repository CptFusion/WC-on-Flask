from flask import Flask, render_template


#create Flask Instance
app = Flask(__name__)

# Create a route decorator (What gets displayed when called. NOT SCREENS)-------------


@app.route('/')

def index():
	return "<h1>Main Page Holder<h1>"

# TO create a template(Screen) you need to create a new folder create a new folder from top directory (fusionweb) and call it "templates"----
# from templates, create new file and making sure its the main active tab, click file>save as>and name your screen with .html at the end-----
# To access the screen you need to return render_template("nameoffile.html")


@app.route('/login')
def login():
	return render_template("loginscreen.html")


@app.route('/greeting')
def greeting():
	return render_template("greetingscreen.html")


@app.route('/customerlist')
def customerlist():
	return render_template("customerlist.html")




#Create custom error pages


#invalid url//page not found

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404



#Internal Server Error

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500