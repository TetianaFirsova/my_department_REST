from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from werkzeug.exceptions import abort

employee = Blueprint("employee", __name__)
service_url='http://127.0.0.1:5002/api/employees'


@employee.route('/employee')
def emp_index():
    response = requests.get(service_url)
    emp_data = response.json()
    return render_template("employees.html", employees=emp_data['data'])


@employee.route('/employee/<int:emp_id>')
def emp(emp_id):
    response = requests.get(service_url+'/'+str(emp_id))
    emp_data = response.json()
    if emp_data['status']=='failed': 
        abort(404)

    return render_template('employee.html', employee_data=emp_data['data'])


@employee.route('/employee/create', methods=('POST',))
def emp_create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        salary = request.form['salary']
        department_id = request.form['department_id']
        email = request.form['email']

        headers = {'Content-type': 'application/json'}
        response = requests.post(service_url, json={"first_name": first_name, "last_name": last_name, "birth_date": birth_date,   "salary": salary, "department_id": department_id, "email": email}, headers=headers)

        if response.status_code in range(200,299):
            flash("Employee was successfully created")

    return redirect(url_for('employee.emp_index'))

#-------------------------------------------------------


@employee.route('/employee/update/<int:emp_id>', methods=['GET', 'POST'])
def emp_update(emp_id):
    pass


@employee.route('/employee/<int:id_emp>/delete', methods=['GET', 'POST'])
def emp_delete(id_emp):
    pass