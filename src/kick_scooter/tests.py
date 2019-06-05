from django.test import TestCase

# Create your tests here.
class TestView(TestCase):

   def test_get_kick_scooter_page(self):
      page = self.client.get("/kick-scooters/")
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'kick_scooter.html')