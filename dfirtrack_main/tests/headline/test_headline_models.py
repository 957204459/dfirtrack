from django.test import TestCase
from dfirtrack_main.models import Headline

class HeadlineModelTestCase(TestCase):
    """ headline model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Headline.objects.create(headline_name='headline_1')

    def test_headline_string(self):

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # compare
        self.assertEqual(str(headline_1), 'headline_1')

    def test_headline_name_label(self):

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # get label
        field_label = headline_1._meta.get_field('headline_name').verbose_name
        # compare
        self.assertEquals(field_label, 'headline name')

    def test_headline_name_length(self):

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # get max length
        max_length = headline_1._meta.get_field('headline_name').max_length
        # compare
        self.assertEquals(max_length, 100)