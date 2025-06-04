import unittest
from unittest.mock import patch

from validation import validate_api_key


class ValidateApiKeyTests(unittest.TestCase):
    """Tests for the validate_api_key function."""

    @patch("validation.genai.GenerativeModel.generate_content")
    @patch("validation.genai.configure")
    def test_empty_key(self, mock_configure, mock_generate):
        result = validate_api_key("")
        self.assertEqual(result, (False, "API key appears invalid"))
        mock_configure.assert_not_called()
        mock_generate.assert_not_called()

    @patch("validation.genai.GenerativeModel.generate_content")
    @patch("validation.genai.configure")
    def test_generate_content_success(self, mock_configure, mock_generate):
        result = validate_api_key("valid-api-key-12345")
        mock_configure.assert_called_once_with(api_key="valid-api-key-12345")
        mock_generate.assert_called_once_with("Test")
        self.assertEqual(result, (True, "API key validated"))

    @patch("validation.genai.GenerativeModel.generate_content", side_effect=Exception("boom"))
    @patch("validation.genai.configure")
    def test_generate_content_failure(self, mock_configure, mock_generate):
        result = validate_api_key("valid-api-key-12345")
        mock_configure.assert_called_once_with(api_key="valid-api-key-12345")
        mock_generate.assert_called_once_with("Test")
        self.assertEqual(result, (False, "Validation failed: boom"))


if __name__ == "__main__":
    unittest.main()
