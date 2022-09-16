import unittest


class TestRequestHandler(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_method(self):
        """
        This test checks if RequestHandler is working properly on a public repo
        """
        from utils.request_handler import RequestHandler
        req = RequestHandler()
        url = "https://api.github.com/repos/golang/go"
        validity, result = req.get(url)
        self.assertEqual(result.status_code, 200)
