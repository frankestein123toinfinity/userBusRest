# Create your tests here.

from django.test import TestCase
from .models import BusDatalist

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
	
	def setUp(self):
		
		self.busDatalist_busId = 73
		self.busDatalist_busStopId = 69
		self.busDatalist = BusDatalist(busId=self.busDatalist_busId, busStopId=self.busDatalist_busStopId)

	def test_model_can_create_a_busDatalist(self):

		old_count = BusDatalist.objects.count()
		self.busDatalist.save()
		new_count = BusDatalist.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

	def setUp(self):

		self.client = APIClient()
		self.busDatalist_data = {'busId': '10', 'busStopId': '18'}
		self.response = self.client.post(
				reverse('create'),
				self.busDatalist_data,
				format="json")

	def test_api_can_create_a_busDatalist(self):

		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_busDatalist(self):
		
		busDatalist = BusDatalist.objects.get()
		response = self.client.get(
			reverse('details'),
			kwargs={'pk': busDatalist.busId},
			format="json")

		self.assertEqual(response.status_code, status.HTTP_201_OK)
		self.assertContains(response, busDatalist)

	def test_api_can_update_busDatalist(self):

		change_busDatalist = {'busStopId': '404'}
		res = self.client.put(
			reverse('details', kwargs={'pk': busDatalist.busId}),
			change_busDatalist,
			format="json")

		self.assertEqual(res.status_code, status.HTTP_201_OK)

	def test_api_can_delete_busDatalist(self):

		busDatalist = busDatalist.objects.get()
		response = self.client.delete(
			reverse('details', kwargs={'pk': busDatalist.busId}),
			format="json",
			follow=True)

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)