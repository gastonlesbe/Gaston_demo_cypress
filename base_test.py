# base_test.py

class BaseTest:
    def assert_text_contains(self, actual_text, expected_text):
        assert expected_text in actual_text