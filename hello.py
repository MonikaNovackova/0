from flask import Flask, render_template, request

app=Flask("MyApp")

@app.route("/")
def helloW():
    return "Hello world"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html",name=name.title())


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print form_data["email"]
    return "All ok. Your email is:"+ form_data["email"]


app.run(debug=True)
print("test")
