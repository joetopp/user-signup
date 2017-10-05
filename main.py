from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome")
def welcome():
    username = request.args.get("username")

    return render_template('welcome.html', username=cgi.escape(username))

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/", methods=['POST'])
def feedback():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    #Initialize Error Messages
    namerr = ""
    paserr = ""
    vererr = ""
    mailerr = ""

    #TODO: Build out error messages

    #If there are no errors, go to the welcome screen
    if namerr == "" and paserr =="" and vererr == "" and mailerr == "":
        return redirect("/welcome?username=" + username)

    return render_template('base.html', namerr=namerr, paserr=paserr, vererr=vererr, mailerr=mailerr)

app.run()