from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# our data list
data_list = [
    {
    "id" : "1",
    "name":"Shaheer",
    "value": 76
    },
    {
    "id" : "2",
    "name":"Ashhad",
    "value": 1000
    },
        ]

# default path
@app.route('/')
def index():
    return render_template('index.html', data_list=data_list)

# path for data submission
@app.route('/submit', methods=['POST'])
def create():
    try:
        if request.method == 'POST':
            name = request.form['name']
            value = request.form['data_value']
        
            data = {'name': name, 'value': value}

            data_list.append(data)
            
            return {"message" : "Data has been added"}
        
    except NameError:
        return {"message" : "OOPs an Error Occured!"}
    
    return redirect('/')
    


if __name__ == '__main__':
    app.run(debug=True)