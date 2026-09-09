import unittest
from unittest.mock import Mock, patch

import password_checker


class TestPasswordChecker(unittest.TestCase):
    def test_get_password_leaks_count_returns_match_count(self):
        response = Mock(text='ABCDEF:42\n123456:7')

        count = password_checker.get_password_leaks_count(response, 'ABCDEF')

        self.assertEqual(count, '42')

    def test_get_password_leaks_count_returns_zero_when_not_found(self):
        response = Mock(text='ABCDEF:42\n123456:7')

        count = password_checker.get_password_leaks_count(response, 'NOTFOUND')

        self.assertEqual(count, 0)

    @patch('password_checker.request_api_data')
    def test_pwned_api_check_hashes_password_and_checks_hash_tail(self, mock_request):
        mock_request.return_value = Mock(
            text='1E4C9B93F3F0682250B6CF8331B7EE68FD8:100\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:1'
        )

        count = password_checker.pwned_api_check('password')

        mock_request.assert_called_once_with('5BAA6')
        self.assertEqual(count, '100')

    @patch('password_checker.requests.get')
    def test_request_api_data_raises_error_for_unsuccessful_request(self, mock_get):
        mock_get.return_value = Mock(status_code=500)

        with self.assertRaises(RuntimeError):
            password_checker.request_api_data('ABCDE')

        mock_get.assert_called_once_with(
            'https://api.pwnedpasswords.com/range/ABCDE', timeout=10
        )


if __name__ == '__main__':
    unittest.main()
