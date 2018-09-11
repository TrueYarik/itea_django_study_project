from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import first_name_validation, last_name_validation, phone_validation, Student, Teacher


class TeacherModelTests(TestCase):

    def test_teacher_creation_and_commiting_into_database(self):
        teacher = Teacher(
            first_name='Kris',
            last_name='Yors',
            email='testmail@teachers.com',
            phone_number='+380976452847',
            subject='Test Subject'
        )
        teacher.save()

        teacher_from_database = Teacher.objects.get(id=teacher.id)

        self.assertEqual(teacher_from_database.first_name, 'Kris')
        self.assertEqual(teacher_from_database.last_name, 'Yors')
        self.assertEqual(teacher_from_database.email, 'testmail@teachers.com')
        self.assertEqual(teacher_from_database.phone_number, '+380976452847')
        self.assertEqual(teacher_from_database.subject, 'Test Subject')


class StudentModelTests(TestCase):

    def test_student_creation_and_commiting_into_database(self):
        student = Student(
            first_name='George',
            last_name='Korn',
            email='k.george@students.com',
            phone_number='+80931264578',
            avg_mark=99
        )
        student.save()

        student_from_database = Student.objects.get(id=student.id)

        self.assertEqual(student_from_database.first_name, 'George')
        self.assertEqual(student_from_database.last_name, 'Korn')
        self.assertEqual(student_from_database.email, 'k.george@students.com')
        self.assertEqual(student_from_database.phone_number, '+80931264578')
        self.assertEqual(student_from_database.avg_mark, 99)


class PersonValidatorsTests(TestCase):

    def test_phone_validation(self):

        # without '+'
        self.assertRaises(ValidationError, phone_validation, '123456789')

        # with letters
        self.assertRaises(ValidationError, phone_validation, '+1234567ddd89')

        # less than 9 digits
        self.assertRaises(ValidationError, phone_validation, '+12345678')

        # less than 13 digits
        self.assertRaises(ValidationError, phone_validation, '+12345678901234')

        # fields correctly
        self.assertEqual(None, phone_validation('+380974563366'))
        self.assertEqual(None, phone_validation('+123456789'))
        self.assertEqual(None, phone_validation('+1234567890123'))



    def test_first_name_validation(self):

        # encounered forbidden symbols or numbers
        self.assertRaises(ValidationError, first_name_validation, 'Cristi@n')
        self.assertRaises(ValidationError, first_name_validation, 'Jack(junior)')
        self.assertRaises(ValidationError, first_name_validation, 'Jack+Jill')
        self.assertRaises(ValidationError, first_name_validation, 'Cris&George')
        self.assertRaises(ValidationError, first_name_validation, 'Ir!na')
        self.assertRaises(ValidationError, first_name_validation, 'Korel,sdfdsf')
        self.assertRaises(ValidationError, first_name_validation, 'Korel,sdfsdf')

        # test correct inserts
        self.assertEqual(None, first_name_validation('John Huan Kim'))
        self.assertEqual(None, first_name_validation('John Huan'))
        self.assertEqual(None, first_name_validation('Huan'))

    def test_last_name_validation(self):
        # encountered forbidden symbols or numbers
        self.assertRaises(ValidationError, last_name_validation, 'Cristi@n')
        self.assertRaises(ValidationError, last_name_validation, 'Jack(junior)')
        self.assertRaises(ValidationError, last_name_validation, 'Jack+Jill')
        self.assertRaises(ValidationError, last_name_validation, 'Cris&George')
        self.assertRaises(ValidationError, last_name_validation, 'Ir!na')
        self.assertRaises(ValidationError, last_name_validation, 'Korel sdfdsf')
        self.assertRaises(ValidationError, last_name_validation, 'Korel,sdfsdf')

        # test right inserts
        self.assertEqual(None, last_name_validation('John-Huan'))
        self.assertEqual(None, last_name_validation('Huan'))



