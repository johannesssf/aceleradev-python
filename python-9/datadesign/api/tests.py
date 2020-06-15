from django.test import TestCase
from django.utils import timezone

from api.models import User, Agent, Group, Event, GroupUser


class UserModelTestCase(TestCase):
    def test_user_creation(self):
        user = User(
            name='Johannes',
            password='12345678',
            last_login=timezone.now(),
            email='johannes@email.com',
        )
        user.save()
        self.assertEqual(User.objects.get(pk=user.pk).name, 'Johannes')
    

class AgentModelTestCase(TestCase):
    def test_agent_creation(self):
        agent = Agent(
            name='CloudVM',
            status=True,
            env='01234567890123456789',
            version='12345',
            address='10.0.0.1',
        )
        agent.save()
        self.assertEqual(Agent.objects.get(pk=agent.pk).name, 'CloudVM')


class GroupModelTestCase(TestCase):
    def test_group_creation(self):
        group = Group(name='Group Test')
        group.save()
        self.assertEqual(Group.objects.get(pk=group.pk).name, 'Group Test')


class EventModelTestCase(TestCase):
    def test_event_creation(self):
        user = User(
            name='Johannes',
            password='12345678',
            last_login=timezone.now(),
            email='johannes@email.com',
        )
        user.save()
        
        agent = Agent(
            name='CloudVM',
            status=True,
            env='01234567890123456789',
            version='12345',
            address='10.0.0.1',
        )
        agent.save()

        event = Event(
            level='none',
            data='Some data test',
            arquivado=False,
            date=timezone.now(),
            agent=agent,
            user=user,
        )
        event.full_clean()
        event.save()
        ev = Event.objects.get(pk=event.pk)
        self.assertEqual(event.level, ev.level)
        self.assertEqual(event.agent.name, ev.agent.name)
        self.assertEqual(event.user.name, ev.user.name)


class GroupUserModelTestCase(TestCase):
    def test_group_user_creation(self):
        group = Group(name='Group Test')
        group.save()
        user = User(
            name='Johannes',
            password='12345678',
            last_login=timezone.now(),
            email='johannes@email.com',
        )
        user.save()
        group_user = GroupUser(
            group=group,
            user=user
        )
        group_user.save()

        gu = GroupUser.objects.get(pk=group_user.pk)
        self.assertEqual(user.name, gu.user.name)
        self.assertEqual(group.name, gu.group.name)

