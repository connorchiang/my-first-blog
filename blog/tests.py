from django.urls import resolve,reverse
from django.test import TestCase
from django.http import HttpRequest
from .models import Post,Cv
from .forms import PostForm,CvForm
from django.contrib.auth.models import User
from .views import post_list,cv_detail, cv_edit  

class HomePageTest(TestCase):

    def setUp(self):
        """Add some objects to the database that all tests will need."""
        self.user = User.objects.create_superuser(
            username='admin', email='', password='admin'
        )

        self.cv = Cv.objects.create(
            title = '1', text = '1',
        contact_details = '1', educational_background = '1',
        award = '1', research_experience = '1', community_services = '1', skills = '1',
        )

        self.client.login(username='admin', password='admin')


    def test_uses_cv_template(self):

        cv_url = reverse("cv_detail", kwargs={"pk": self.cv.pk})
        response = self.client.get(cv_url)
        self.assertTemplateUsed(response, 'blog/cv_detail.html')


    def test_saving_cv(self): 

        saved_cv = Cv.objects.all()
        self.assertEqual(saved_cv.count(), 1)

        first_cv = saved_cv[0]
        first_cv.text = 'The first Cv'
        first_cv.save()


        self.assertEqual(first_cv.text, 'The first Cv')


    def test_superuser_can_edit_old_blog_post(self):

        new_title = 'Test Title'
        new_contact = 'Name'

        response = self.client.post(reverse('cv_edit', kwargs={'pk': self.cv.pk}), {
            'title': new_title,
            'text': '1',
            'contact_details' : new_contact,
            'educational_background' : '1',
            'award' : '1',
            'research_experience' : '1',
            'community_services' : '1' ,
            'skills' : '1',
        }, follow=True)

        self.assertRedirects(response, reverse('cv_detail', kwargs={'pk': self.cv.pk}))
        self.assertContains(response, new_title)
        self.assertContains(response, new_contact)


