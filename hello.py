from flask import Flask, render_template, request, url_for

app=Flask("MyApp")

@app.route("/")
def helloW():
    return "Hello world"

@app.route("/research")
def get_research_page():
    return render_template("research.html")

@app.route("/index")
def get_main_page():
    return render_template("index.html")

@app.route("/teaching")
def get_teaching_page():
    return render_template("teaching.html")

@app.route("/programming")
def get_programming_page():
    return render_template("programming.html")



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print form_data["email"]
    return "All ok. Your email is:"+ form_data["email"]




@app.route("/signup2", methods=["POST"])
def returnhome():
    form_data=request.form
    v_email=form_data["email"]
    return render_template("programming.html",v_email=v_email)



print("test")

@app.route('/index')
@app.route('/')
def index():
    return 'you are in the index page'

app.run(debug=True)