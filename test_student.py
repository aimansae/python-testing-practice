import unittest
from student import Student

# always required


class TestStudents(unittest.TestCase):
    
    

    def setUp(self):
        print('setup')
        self.student = Student('Jhon', 'Doe')

    # full name testisng

    def test_full_name(self):
        # create an instance of student class with arguments
        print('test_full_name')

        self.assertEqual(self.student.full_name, 'Jhon Doe')

    def test_alert_santa(self):
        print('test_alert_santa')

        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'jhon.doe@email.com')

        # always required
if __name__ == '__main__':
    unittest.main()
