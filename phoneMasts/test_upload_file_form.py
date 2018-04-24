from django.test import TestCase
# from unittest.mock import MagicMock
# from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import UploadFileForm


class UploadFileFormTests(TestCase):

    # def test_upload_file_form_valid_with_good_data(self):

    #     mock_file = MagicMock(spec=File)
    #     form = UploadFileForm(files={'my_file': mock_file})

    #     self.assertTrue(form.is_valid())

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
