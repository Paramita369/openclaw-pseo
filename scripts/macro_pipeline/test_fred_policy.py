import unittest

from fred_policy import enforce_fred_api_requirement


class FredPolicyTests(unittest.TestCase):
    def test_strict_mode_requires_api_key(self):
        with self.assertRaises(RuntimeError):
            enforce_fred_api_requirement(strict=True, fred_api_key='', fetch_statuses={'CPI': 'api'})

    def test_strict_mode_rejects_non_api_fetches(self):
        with self.assertRaises(RuntimeError):
            enforce_fred_api_requirement(strict=True, fred_api_key='KEY', fetch_statuses={'CPI': 'csv'})

    def test_non_strict_mode_allows_missing_key(self):
        enforce_fred_api_requirement(strict=False, fred_api_key='', fetch_statuses={'CPI': 'csv'})


if __name__ == '__main__':
    unittest.main()
