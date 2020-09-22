from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostTests(TestCase):

    def setUp(self):
            self.user = get_user_model().objects.create_user(
                username='mais',
                email='maisjamil17118@gmail.com',
                password='1234'
            )

            self.post =Post.objects.create(
                title='python',
                author=self.user,
                body='python language',
            )


    def test_Model_str(self):
        post = Post('python','mais','python language')
        self.assertEqual(str(post), post.title)
    

# _______________________________________________________

    def test_home_status(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
# _______________________________________________________

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

# _______________________________________________________

    def test_details_view(self):
        response = self.client.get(reverse('post_details', args='1'))
        self.assertEqual(response.status_code, 200)

# _______________________________________________________

    def test_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'css',
            'author': self.user,
            'body': 'css css css',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        self.assertContains(response, 'css')
        self.assertContains(response, 'css css css')

# _______________________________________________________

    
    def test_update_view(self):
        response = self.client.post(reverse('post_update', args='1'), {
            'title': 'something',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'something')

# _______________________________________________________

    def test_delete_view(self):
        response = self.client.get(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code, 200)
# _______________________________________________________