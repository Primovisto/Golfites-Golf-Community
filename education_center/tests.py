from django.test import TestCase
from education_center.views import education_post_list
from django.urls import resolve


class EducationPageTest(TestCase):

    def test_blog_page_status_code_is_ok(self):
        blog_page = self.client.get('/education_center/')
        self.assertEquals(blog_page.status_code, 200)

    def test_blog_page_status_code_is_not_404(self):
        blog_page = self.client.get('/education_center/')
        self.assertNotEquals(blog_page.status_code, 404)

    def test_blog_page_status_code_is_not_500(self):
        blog_page = self.client.get('/education_center/')
        self.assertNotEquals(blog_page.status_code, 500)

    def test_blog_page(self):
        blog_page = resolve('/education_center/')
        self.assertEqual(blog_page.func, education_post_list)

    def test_check_content_is_correct(self):
        blog_page = self.client.get('/education_center/')
        self.assertTemplateUsed(blog_page, "education_center/education_blogposts.html")