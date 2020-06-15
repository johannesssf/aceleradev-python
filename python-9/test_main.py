import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import User, Agent, Group, Event, GroupUser


class TestChallenge9(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="Jose",
            email="jose@gmail.com",
            password="xxxxxxxxxxxxxxxxxxxxxxx"
        )
        self.agent = Agent.objects.create(
            name="Machine1",
            address="192.168.1.1",
            status=True,
            env="prod",
            version="1.1.1"
        )
        group = Group.objects.create(name="Admin")
        GroupUser.objects.create(user=self.user, group=group)
        Event.objects.create(
            level="CRITICAL",
            data="django.core.exceptions.ValidationError",
            user=self.user,
            agent=self.agent,
            arquivado=False
        )

    def test_1(self):
        user = User.objects.get(name="Jose")
        self.assertEqual(user.email, "jose@gmail.com")

    def test_2(self):
        agent = Agent.objects.get(name="Machine1")
        self.assertEqual(agent.name, "Machine1")

    def test_3(self):
        group = Group.objects.get(name="Admin")
        self.assertEqual(group.name, "Admin")

    def test_4(self):
        event = Event.objects.get(level="CRITICAL")
        self.assertEqual(event.level, "CRITICAL")
    
    def test_user_password_less_then_eight(self):
        user = User.objects.create(
            name="Jose",
            email="jose@gmail.com",
            password="xxxxx"
        )
        with self.assertRaises(ValidationError):
            try:
                user.full_clean()
            except ValidationError as ex:
                print(ex.error_dict)
                raise ex

    def test_user_invalid_email(self):
        user = User.objects.create(
            name="Jose",
            email="notaemail.com",
            password="xxxxxxxxxxxxxxx"
        )
        with self.assertRaises(ValidationError):
            try:
                user.full_clean()
            except ValidationError as ex:
                print(ex.error_dict)
                raise ex

    def test_aget_invalid_address(self):
        agent = Agent.objects.create(
            name="Machine1",
            address="192.168.x.x",
            status=True,
            env="prod",
            version="1.1.1"
        )
        with self.assertRaises(ValidationError):
            try:
                agent.full_clean()
            except ValidationError as ex:
                print(ex.error_dict)
                raise ex
    
    def test_event_invalid_level(self):
        event = Event.objects.create(
            level="INVALID",
            data="django.core.exceptions.ValidationError",
            user=self.user,
            agent=self.agent,
            arquivado=False
        )
        with self.assertRaises(ValidationError):
            try:
                event.full_clean()
            except ValidationError as ex:
                print(ex.error_dict)
                raise ex
