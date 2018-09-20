import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""was_published_recently should return false for questions with future pub_dates"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)

		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""was_published_recently should return false for questions with pub_date older than 1 day"""
		time = timezone.now() - datetime.timedelta(days=1,seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(),False)

	def test_was_published_recently_with_recent_question(self):
		"""was_published_recently should return True for questions with pub_date within 1 day"""
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

	def notatest(self):
		print("notatest called!")
		self.assertIs(True, True)	#just to see if it gets called
		#does not get called

	def testnotatest(self):
		print("testnotatest called!")
		self.assertIs(True, True)	#just to see if it gets called
		#does get called, so looks for object.test*() to run