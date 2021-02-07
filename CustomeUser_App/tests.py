from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTest(TestCase):
    def test_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('test@test.com','test','test1','test2','testpassword')
        self.assertEqual(super_user.email,'test@test.com')
        self.assertEqual(super_user.username,'test')
        self.assertEqual(super_user.first_name,'test')
        self.assertEqual(super_user.last_name,'test')
        self.assertEqual(super_user.password,'testpassword')
        self.assertEqual(super_user.is_active,'True')
        self.assertEqual(super_user.is_staff,'True')
        self.assertEqual(super_user.is_superuser,'True')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = 'test@user.com',
                username = 'newuser',
                first_name = 'newuser_1',
                last_name = 'newuser_2',
                password = 'testpass1',
                is_superuser = False 
            ) 
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = 'test@user2.com',
                username = 'newuser',
                first_name = 'newuser_1',
                last_name = 'newuser_2',
                password = 'testpass2',
                is_staff = False 
            ) 
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = 'test@user3.com',
                username = 'newuser',
                first_name = 'newuser_1',
                last_name = 'newuser_2',
                password = 'testpass3',
                is_active = False 
            )  

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='a', first_name='first_name', password='password')               
