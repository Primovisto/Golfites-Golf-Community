from django.test import TestCase
from home.views import index
from django.urls import resolve
from accounts.models import User


class HomePageTest(TestCase):
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()

    def test_login(self):
        login = self.client.login(username='testuser', password='letmein')
        self.assertTrue(login)

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, index)

    def test_home_page_uses_index_template(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")