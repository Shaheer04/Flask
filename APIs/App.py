from flask import Flask, render_template, request

app = Flask("My First Application")

@app.route('/sample')
def getsamplehtml():
    return render_template ('sample.html')

@app.route('/user/< useranme >', methods=['GET'])
def greetUser(username):
    return render_template ("result.html", username=username )

@app.route('user', methods=['GET'])
def greetUserBasedOnReq():
    username = request.args.get("username")
    return render_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
