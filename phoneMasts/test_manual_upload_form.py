from django.test import TestCase

from .forms import ManualUploadForm


class ManualUploadFormTests(TestCase):

    def test_manual_upload_form_valid_with_good_data(self):
        form_data = {
            'property_name': 'test name',
            'property_address_1': 'address line 1',
            'property_address_2': 'address line 2',
            'property_address_3': 'address line 3',
            'property_address_4': 'address line 4',
            'unit_name': 'test unit name',
            'tenant_name': 'test tenant name',
            'lease_start_date': 'lease start',
            'lease_end_date': 'lease end',
            'lease_years': 7474774,
            'current_rent': 99999.87,
        }

        result = ManualUploadForm(form_data)
        self.assertTrue(result.is_valid())

    def test_manual_upload_form_with_missing_field(self):
        form_data = {
            'property_address_1': 'address line 1',
            'property_address_2': 'address line 2',
            'property_address_3': 'address line 3',
            'property_address_4': 'address line 4',
            'unit_name': 'test unit name',
            'tenant_name': 'test tenant name',
            'lease_start_date': 'lease start',
            'lease_end_date': 'lease end',
            'lease_years': 7474774,
            'current_rent': 99999.87,
        }

        result = ManualUploadForm(form_data)
        self.assertFalse(result.is_valid())

    def test_manual_upload_form_with_wrong_data_type(self):
        form_data = {
            'property_name': 232,
            'property_address_1': 'address line 1',
            'property_address_2': 'address line 2',
            'property_address_3': 'address line 3',
            'property_address_4': 'address line 4',
            'unit_name': 435,
            'tenant_name': 'test tenant name',
            'lease_start_date': 'lease start',
            'lease_end_date': 'lease end',
            'lease_years': 7474774,
            'current_rent': 'bad string',
        }

        result = ManualUploadForm(form_data)
        self.assertFalse(result.is_valid())

    def test_manual_upload_form_ignores_extra_data_field(self):
        form_data = {
            'extra_field': 'SURPRISE',
            'property_name': 'test name',
            'property_address_1': 'address line 1',
            'property_address_2': 'address line 2',
            'property_address_3': 'address line 3',
            'property_address_4': 'address line 4',
            'unit_name': 'test unit name',
            'tenant_name': 'test tenant name',
            'lease_start_date': 'lease start',
            'lease_end_date': 'lease end',
            'lease_years': 7474774,
            'current_rent': 99999.87,
        }

        result = ManualUploadForm(form_data)
        self.assertTrue(result.is_valid())
