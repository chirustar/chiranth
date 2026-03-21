from flask import Flask,render_template,request,redirect
import business_layer as bl

app = Flask(__name__)  # creates an instance of the Flask class

@app.route('/home')
def home():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def add_employee():
    emp = {
        "id": request.form['id'],
        "name": request.form['name'],
        "age": request.form['age'],
        "department": request.form['department']
    }
    bl.add_employee(emp)
    return redirect('/employees')

@app.route('/employees')
def employees():
    data = bl.get_all()
    return {"employees": data}

@app.route('/employee/<emp_id>')
def get_employee(emp_id):
    emp = bl.get_by_id(emp_id)
    return emp if emp else {"message": "Not found"}

@app.route('/update/<emp_id>', methods=['POST'])
def update(emp_id):
    new_data = request.form.to_dict()
    bl.update_employee(emp_id, new_data)
    return {"message": "Updated"}

@app.route('/delete/<emp_id>')
def delete(emp_id):
    bl.delete_employee(emp_id)
    return {"message": "Deleted"}

if __name__ == '__main__':
    app.run(debug=True)