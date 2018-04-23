from django.test import TestCase
from unittest.mock import Mock

from .forms import UploadFileForm


class UploadFileFormTests(TestCase):

    def test_upload_file_form_valid_with_good_data(self):
        mock_file = Mock(spec=django.core.files.File)
        mock_file.read.return_value = "mock file contents"

        form_data = {
            'my_file': mock_file
        }

        result = UploadFileForm(form_data)
        self.assertTrue(result.is_valid())

    def test_upload_file_form_with_no_data(self):

        form_data = {}

        result = UploadFileForm(form_data)
        self.assertFalse(result.is_valid())

    def test_upload_file_form_with_bad_data(self):

        form_data = {
            'data': 'this is wrong'
        }

        result = UploadFileForm(form_data)
        self.assertFalse(result.is_valid())
