from unittest import TestCase

from scripts.main import lambda_handler

class SampleTestCase(TestCase):

    def test_lambda_handler(self):
        lambda_handler(None, None)

