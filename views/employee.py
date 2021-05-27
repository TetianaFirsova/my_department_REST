from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from werkzeug.exceptions import abort
from config import serv_url

employee = Blueprint("employee", __name__)
service_url=serv_url+'/api/employees'      #'http://depemp-service.herokuapp.com/api/employees'


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
        return abort(404)

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


@employee.route('/employee/search', methods=['GET','POST'])
def search_by_date():
    if request.method == 'POST':
        b_date = request.form['search_date']

        if not b_date: 
            flash("Birth date for search is empty")
            return redirect(url_for('employee.emp_index'))

        response = requests.get(service_url+'/search/'+str(b_date))
        emp_data = response.json()
        if emp_data['status']=='failed': 
            flash(emp_data['message'])
            return redirect(url_for('employee.emp_index'))  #abort(404)

    return render_template('search_result.html', employees_data=emp_data['data'])


@employee.route('/employee/search_between', methods=['GET','POST'])
def search_between_dates():
    if request.method == 'POST':
        start_b_date = request.form['start_search_date']
        end_b_date = request.form['end_search_date']

        response = requests.get(service_url+'/search_between/'+str(start_b_date)+','+str(end_b_date))
        emp_data = response.json()
        if emp_data['status']=='failed': 
            flash(emp_data['message'])
            return redirect(url_for('employee.emp_index'))  #abort(404)

    return render_template('search_result.html', employees_data=emp_data['data'])


@employee.route('/employee/update/<int:emp_id>', methods=['GET', 'POST'])
def emp_update(emp_id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        salary = request.form['salary']
        department_id = request.form['department_id']
        email = request.form['email']

        headers = {'Content-type': 'application/json'}
        response = requests.put(service_url, json={"id_emp": emp_id, "first_name": first_name, "last_name": last_name, "birth_date": birth_date, "salary": salary, "department_id": department_id, "email": email}, headers=headers)

        if response.status_code in range(200,299):
            flash("Employee was successfully updated")

    return redirect(url_for('employee.emp', emp_id=emp_id))


@employee.route('/employee/<int:emp_id>/delete', methods=['GET', 'POST'])
def emp_delete(emp_id):
    if request.method == 'POST':
        headers = {'Content-type': 'application/json'}
        response = requests.delete(service_url, json={"id_emp": emp_id}, headers=headers)

        if response.status_code in range(200,299):
            flash("Employee was successfully deleted")

    return redirect(url_for('employee.emp_index'))