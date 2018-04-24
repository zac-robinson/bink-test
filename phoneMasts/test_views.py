from django.test import TestCase
from django.urls import reverse
from phoneMasts.models import PhoneMasts


def create_phone_mast(field_name=None, override_value=None):
    mast = {
        'property_name': 'test property',
        'property_address_1': 'address 1',
        'property_address_2': 'address 2',
        'property_address_3': 'address 3',
        'property_address_4': 'address 4',
        'unit_name': 'unit_name',
        'tenant_name': 'tenant_name',
        'lease_start_date': '29-Oct-1992',
        'lease_end_date': '29-Oct-2018',
        'lease_years': 26,
        'current_rent': 1500
    }

    if field_name is not None and override_value is not None:
        mast[field_name] = override_value

    return PhoneMasts.objects.create(
        property_name=mast['property_name'],
        property_address_1=mast['property_address_1'],
        property_address_2=mast['property_address_2'],
        property_address_3=mast['property_address_3'],
        property_address_4=mast['property_address_4'],
        unit_name=mast['unit_name'],
        tenant_name=mast['tenant_name'],
        lease_start_date=mast['lease_start_date'],
        lease_end_date=mast['lease_end_date'],
        lease_years=mast['lease_years'],
        current_rent=mast['current_rent']
    )


class IndexViewTest(TestCase):

    def test_no_data(self):
        response = self.client.get(reverse('phoneMasts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No mast data available.")
        self.assertQuerysetEqual(response.context['masts_by_lease_amount'], [])

    def test_with_valid_phone_mast(self):
        create_phone_mast()
        response = self.client.get(reverse('phoneMasts:index'))
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: test property>']
        )


# class UploadFileViewTest(TestCase):
#
#     def test_no_data(self):
#         response = self.client.post(reverse('phoneMasts:upload_file'))
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No mast data available.")
#         self.assertQuerysetEqual(response.context['masts_by_lease_amount'], [])
#
#     def test_with_valid_phone_mast(self):
#         create_phone_mast()
#         response = self.client.get(reverse('phoneMasts:index'))
#         self.assertQuerysetEqual(
#             response.context['masts_by_lease_amount'],
#             ['<PhoneMasts: test property>']
#         )
