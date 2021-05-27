from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from werkzeug.exceptions import abort
from config import serv_url


department = Blueprint("department", __name__)
service_url=serv_url+'/api/departments'


@department.route('/department')
def dep_index():
    response = requests.get(service_url)
    dep_data = response.json()
    return render_template("departments.html",departments=[dep_data['data'],dep_data['avg_sal']])


@department.route('/department/<int:dep_id>')
def dep(dep_id):
    response = requests.get(service_url+'/'+str(dep_id))
    dep_data = response.json()
    if dep_data['status']=='failed': 
        abort(404)

    return render_template('department.html', departments=[dep_data['dep_data'], dep_data['dep_employees'], dep_data['average salary']])


@department.route('/department/create', methods=('POST',))
def dep_create():
    if request.method == 'POST':
        dep_name = request.form['dep_name']
        description = request.form['description']

        headers = {'Content-type': 'application/json'}
        response = requests.post(service_url, json={"dep_name": dep_name, "description": description}, headers=headers)
        
        if response.status_code in range(200,299):
            flash("Department was successfully created")

    return redirect(url_for('department.dep_index'))


@department.route('/department/<int:dep_id>/update', methods=['GET', 'POST'])
def dep_update(dep_id):
    if request.method == 'POST':
        dep_name = request.form['dep_name']
        description = request.form['description']

        headers = {'Content-type': 'application/json'}
        response = requests.put(service_url, json={"id_dep": dep_id, "dep_name": dep_name, "description": description}, headers=headers)

        if response.status_code in range(200,299):
            flash("Department was successfully updated")

    return redirect(url_for('department.dep', dep_id=dep_id))


@department.route('/department/<int:dep_id>/delete', methods=['GET', 'POST'])
def dep_delete(dep_id):
    if request.method == 'POST':
        headers = {'Content-type': 'application/json'}
        response = requests.delete(service_url, json={"id_dep": dep_id}, headers=headers)

        if response.status_code in range(200,299):
            flash("Department was successfully deleted")

    return redirect(url_for('department.dep_index'))