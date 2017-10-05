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
    if username == "":
        namerr = "You must enter a username"
    elif username.find(" ") != -1 or len(username) < 3:
        namerr = "That's not a valid username"

    if password == "":
        paserr = "You must enter a password"
    elif password.find(" ") != -1 or len(password) < 3:
        paserr = "That's not a valid password"
    
    if verify == "":
        vererr = "You must verify your password"
    elif verify != password:
        vererr = "Passwords don't match"

    if email != "" and email.find("@") == -1 and email.find(".") == -1:
        mailerr = "That's not a valid email"

    #If there are no errors, go to the welcome screen
    if namerr == "" and paserr =="" and vererr == "" and mailerr == "":
        return redirect("/welcome?username=" + username)

    return render_template('base.html', namerr=namerr, paserr=paserr, vererr=vererr, mailerr=mailerr)

app.run()