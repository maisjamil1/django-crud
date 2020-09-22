from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class PostTests(TestCase):
    def test_home_status(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)
