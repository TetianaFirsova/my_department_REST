Imaginary University

DESCRIPTION

&quot;my\_department\_REST&quot; is a simple web application for managing departments and employees. This web application uses web service &quot;service&quot; for storing data and reading from database. The Web application is deployed on Heroku with name &quot;imaginary-university&quot; and available at https://imaginary-university.herokuapp.com/ The Web service is also deployed on Heroku with name &quot;depemp-service&quot; and available at https://imaginary-university.herokuapp.com/ For local running the web app and web service one should use addresses [https://127.0.0.1:5000](https://127.0.0.1:5000/) and [https://127.0.0.1:5002](https://127.0.0.1:5002/) respectively.

The web application should allow:

- display a list of all departments and the average salary (calculated automatically) for these departments

- display information about chosen department including a list of its employees and an indication of the salary for each employee

- display a list of all employees and a search field to search for employees born on a certain date or in the period between dates

- display information about chosen employee

- change (add / edit / delete) the above data

-###1. Home

Display greeting title and greeting image.

_**Main scenario:**_

- User selects menu tab &quot;Home&quot;;
- Application displays greeting page.

    <p align="center">
    <img src="/documentation/mockups/home_page.png">
    </p>

**2. Departments**

**2.1. Display a list of all departments**

This page is intended for viewing list of all departments and creating the new one.

_**Main scenario:**_

- User selects menu tab &quot;Departments&quot;;
- Application displays list of departments and automatically calculated average salary for these departments

    <p align="center">
    <img src="/documentation/mockups/departments_list.png">
    </p>

_**View selected department:**_

- User selects chosen department and presses its name;
- Application will show the page with all information about this department (see pict 1).

_**Create new department:**_

- User clicks the &quot;New department&quot; button in the right top;
- Application displays form to enter department data;
- User enters department&#39;s data and presses &quot;Add department&quot; button;
- Data sends to web service and adds to database;
- Created department appears in list of all departments;
- In step3 if user presses &quot;Close&quot; button, then any department is created.

    <p align="center">
    <img src="/documentation/mockups/add_department.png">
    </p>

**2.2 Display selected department**

This page is intended for viewing information about chosen department and editing/deleting this department

    <p align="center">
    <img src="/documentation/mockups/department_page.png">
    </p>
Pict. 1

_**Edit department:**_

- User clicks the &quot;Edit&quot; button in the right bottom;
- Application displays form to edit department data;
- User update department&#39;s data and presses &quot;Update&quot; button;
- Data sends to web service and updates in database;
- Information about department is updated in department page;
- In step3 if user presses &quot;Close&quot; button, then any department was not updated. 

    <p align="center">
    <img src="/documentation/mockups/update_department.png">
    </p>

_**Delete department:**_

- User clicks the &quot;Delete&quot; button in the right bottom;
- Application displays confirmation dialog &quot;Please confirm delete department&quot;;
- User confirms the removal of the department.
- Request is send to web service, department is deleted from database;
- If department record is successfully deleted, then list of departments without deleted department is displaying.
- In step3 If user denied deletion, then department is not deleted.

_**Back to departments:**_

- User presses &quot;Back to departments&quot; reference;
- Application will show the page with list of all departments.

_**View selected employee:**_

- User presses selected employee reference in the department;
- Application will show the page with information about chosen employee.

**3. Employees**

**3.1. Display a list of all employees**

This page is intended for viewing list of all employees, creating the new one, searching for employees born on a certain date or in the period between dates

_**Main scenario:**_

- User selects menu tab &quot;Employees&quot;;
- Application displays list of employees.

    <p align="center">
    <img src="/documentation/mockups/employees_list.png">
    </p>

_**View selected employee:**_

- User selects chosen employee and presses its name;
- Application will show the page with all information about this employee (see pict 2).

_**Create new employee:**_

- User clicks the &quot;New employee&quot; button in the right top;
- Application displays form to enter employee data;
- User enters employee&#39;s data and presses &quot;Add&quot; button;
- Data sends to web service and adds to database;
- Created employee appears in list of all employees;
- In step3 if user presses &quot;Close&quot; button, then any employee is created.

    <p align="center">
    <img src="/documentation/mockups/add_employee.png">
    </p>

_**Search for employees by date:**_

- User sets a date of employee birth in top search field and presses &quot;Search&quot; button;
- Application will show the page with all employees was born on this date.

    <p align="center">
    <img src="/documentation/mockups/search_results.png">
    </p>

_**Search for employees by period between dates:**_

- User sets a start and end dates in bottom search fields and presses &quot;Search&quot; button;
- Application will show the page with all employees was born in the entered period.

**3.2 Display selected employee**

This page is intended for viewing information about chosen employee and editing/deleting this employee

    <p align="center">
    <img src="/documentation/mockups/employee_page.png">
    </p>

pict. 2.

_**Edit employee:**_

- User clicks the &quot;Edit&quot; button in the right bottom;
- Application displays form to edit employee data;
- User update employee&#39;s data and presses &quot;Update&quot; button;
- Data sends to web service and updates in database;
- Information about employee is updated in employee page;
- In step3 if user presses &quot;Close&quot; button, then any employee was not updated.

    <p align="center">
    <img src="/documentation/mockups/update_employee.png">
    </p>

_**Delete employee:**_

- User clicks the &quot;Delete&quot; button in the right bottom;
- Application displays confirmation dialog &quot;Please confirm delete employee&quot;;
- User confirms the removal of the employee.
- Request is send to web service, employee is deleted from database;
- If employee record is successfully deleted, then list of employees without deleted employee is displaying.
- In step3 If user denied deletion, then employee is not deleted.

_**Back to departments:**_

- User presses &quot;Back to employees&quot; reference;
- Application will show the page with list of all employees.

_**View information about department where employee working in:**_

- User presses &quot;Department id&quot; field value;
- Application will show the page with information about corresponding department.