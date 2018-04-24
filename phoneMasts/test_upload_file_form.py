from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import UploadFileForm


class UploadFileFormTests(TestCase):

    # def test_upload_file_form_valid_with_good_data(self):

    #     my_model.file_field = SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!')
    #     mock_file = MagicMock(spec=File)
    #     form = UploadFileForm(files={'my_file': mock_file})

    #     file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
    #     form = MyForm(files=file_dict)
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
