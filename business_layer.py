from file_handler import init_file, read_data, write_data, append_data

init_file()

def add_employee(emp):
    append_data(emp)

def get_all():
    return read_data()

def get_by_id(emp_id):
    employees = read_data()
    for emp in employees:
        if emp['id'] == emp_id:
            return emp
    return None

def update_employee(emp_id, new_data):
    employees = read_data()
    for emp in employees:
        if emp['id'] == emp_id:
            emp.update(new_data)
            break
    write_data(employees)

def delete_employee(emp_id):
    employees = read_data()
    employees = [emp for emp in employees if emp['id'] != emp_id]
    write_data(employees)