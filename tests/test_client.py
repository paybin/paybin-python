import unittest
from unittest.mock import patch, MagicMock
from paybin import PaybinClient, PaybinAPIError

class TestPaybinClient(unittest.TestCase):
    def setUp(self):
        self.client = PaybinClient("pub_key", "sec_key", sandbox=True)

    def test_init(self):
        self.assertEqual(self.client.public_key, "pub_key")
        self.assertEqual(self.client.secret_key, "sec_key")
        self.assertTrue(self.client.base_url.startswith("https://sandbox"))

    @patch('paybin.client.requests.Session.request')
    def test_request_success(self, mock_request):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "code": 200,
            "message": "OK",
            "data": {"foo": "bar"}
        }
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        data = self.client.request("POST", "/test")
        self.assertEqual(data, {"foo": "bar"})

    @patch('paybin.client.requests.Session.request')
    def test_request_api_error(self, mock_request):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "code": 400,
            "message": "Bad Request",
            "data": None
        }
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        with self.assertRaises(PaybinAPIError):
            self.client.request("POST", "/test")

if __name__ == '__main__':
    unittest.main()
