from django.test import TestCase
from django.urls import reverse
from .models import Enquiry

class CorporateSiteTests(TestCase):
    def test_main_pages_load(self):
        for route in ["home", "about", "businesses", "technology", "paint", "projects", "insights", "careers", "partnerships", "contact"]:
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)
    def test_business_detail(self):
        response = self.client.get(reverse("business_detail", args=["technology-it-solutions"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technology &amp; IT Solutions")
    def test_contact_submission_saved(self):
        response = self.client.post(reverse("contact"), {
            "name":"Ada Example", "email":"ada@example.com", "phone":"+2348000000000",
            "enquiry_type":"general", "subject":"Test enquiry", "message":"A genuine question."
        })
        self.assertRedirects(response, reverse("contact"))
        self.assertEqual(Enquiry.objects.count(), 1)
    def test_contact_rejects_invalid_email(self):
        response = self.client.post(reverse("contact"), {
            "name":"Ada", "email":"not-an-email", "enquiry_type":"general",
            "subject":"Test", "message":"Message"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 0)
