"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
django.setup()
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# TODO: Configure your database in settings.py and sync before running tests.

class QuestionModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        django.setup()
        super(QuestionModelTests, cls).setUpClass()

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
