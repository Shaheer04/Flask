from flask import Flask, render_template,request
from Maths.math import summation, subtraction, multiplication

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('main.html')

@app.route('/add')
def add_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    
    return render_template('result.html',result=result)

@app.route('/sub')
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    
    return render_template('result.html',result=result)

@app.route('/mul')
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    
    return render_template('result.html',result=result)





if __name__ == '__main__':
    app.run(debug=True)