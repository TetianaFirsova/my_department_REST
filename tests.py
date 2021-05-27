import unittest
from flask_testing import TestCase
from app import create_app, app


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        return app

class TestViews(TestBase):

    def test_home_view(self):
        """
        Test that homepage is accessible
        """
        response = self.client.get('/')
        self.assert_status(response, 200)

    def test_departments_view(self):
        """
        Test that departments page is accessible
        """
        response = self.client.get('/department')
        self.assert_status(response, 200)

    def test_employees_view(self):
        """
        Test that employees page is accessible
        """
        response = self.client.get('/employee')
        self.assert_status(response, 200)

    def test_existing_department_view(self):
        """
        Test that existing department page is accessible
        """
        response = self.client.get('/department/1')
        self.assert_status(response, 200)

    def test_unexisting_department_view(self):
        """
        Test that unexisting department page returns 404 error
        """
        response = self.client.get('/department/66')
        self.assert_status(response, 404)

    def test_existing_employee_view(self):
        """
        Test that existing employee page is accessible
        """
        response = self.client.get('/employee/1')
        self.assert_status(response, 200)

    def test_unexisting_employee_view(self):
        """
        Test that unexisting employee page returns 404 error
        """
        response = self.client.get('/employee/55')
        self.assert_status(response, 404)

    def test_department_create_view(self):
        response = self.client.get('/department/create')
        self.assert_status(response, 405)

    def test_employee_create_view(self):
        response = self.client.get('/employee/create')
        self.assert_status(response, 405)

    def test_department_update_view(self):
        response = self.client.get('/department/1/update')
        self.assert_status(response, 302)

    def test_employee_update_view(self):
        response = self.client.get('/employee/1/update')
        self.assert_status(response, 404)

    def test_department_delete_view(self):
        response = self.client.get('/department/1/delete')
        self.assert_status(response, 302)

    def test_employee_delete_view(self):
        response = self.client.get('/employee/1/delete')
        self.assert_status(response, 302)

    
if __name__ == '__main__':
    unittest.main()