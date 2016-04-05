from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Plans
from journal import views
from django.views.generic.list import ListView


from django.test import Client
class TestWithClient(TestCase):
	def testWithClienMethod(self):
		c = Client()
		response = c.post('/journal/', {'date': '2016-01-01', 'activity': 'doing', 'description': 'gonna be doing something', 'significance':'im'})
		b = response.status_code
		if b == 200:
			print('ClientMethod added a plan successfully')
		response = c.get('/journal/')
		response.content

class Sometests(TestCase):
	def test1(self):
		"this should fail"			# if KeyError
		Plans.objects.create(activity="wrongDateActivity", date = "2016.01.01")
	def test2(self):
		Plans.objects.create(activity="wrongDateActivity", date = "2016-01-01")
		for i in Plans.objects.all():
			self.a = str(i)
		rightDateformat = "2016-01-01"
		if self.a == rightDateformat:
			print("Test with wrong date frmat should fail")

class NewDayTest(TestCase):
	def testCreatePlan(self):
		print("Test1: Creating new plan...")
		Plans.objects.create(activity="shopping", date = "2015-05-05", description = "im going to buy some new clothes")
		print("Created:", Plans.objects.all())


class UniqueDateTest(TestCase):
	error = False
	A = []
	Duplicates =[]
	for i in Plans.objects.all():	#makeing list which cointain what database contains...
		A.append(str(i))			#... and change vars to strings so it could be count
	for i in A:
		x = A.count(i) 				#if found >=2 same var it adds it to duplicates list
		if x >= 2:
			Duplicates.append(i)
			A.remove(i)
			error = True
	y = len(Duplicates)
	def test_are_any_duplicated_date_plans(self):
		if self.error == False:
			print("Didnt find any duplicated date plans")
		else:
			print("Found ", self.y, " duplicated date plans:", self.Duplicates)
