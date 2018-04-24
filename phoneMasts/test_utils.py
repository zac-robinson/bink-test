from django.test import TestCase
from phoneMasts.utils import *
from phoneMasts.models import PhoneMasts


def create_phone_mast(override_tenant='tenant_name',
                      override_property_name='property_name',
                      override_current_rent=150):

    return PhoneMasts.objects.create(
        property_name=override_property_name,
        property_address_1='property_address_1',
        property_address_2='property_address_2',
        property_address_3='property_address_3',
        property_address_4='property_address_4',
        unit_name='unit_name',
        tenant_name=override_tenant,
        lease_start_date='29-Oct-1992',
        lease_end_date='29-Oct-2018',
        lease_years=26,
        current_rent=override_current_rent
    )


class UtilsTest(TestCase):

    def test_get_mast_dict_no_masts(self):
        result = get_mast_dict()
        self.assertEqual(result, {})

    def test_get_mast_dict_with_mast(self):
        create_phone_mast()
        expected = {
            'tenant_name': 1
        }

        result = get_mast_dict()
        self.assertEqual(result, expected)

    def test_get_mast_dict_single_mast_per_tenant(self):
        create_phone_mast()
        create_phone_mast(override_tenant='second tenant')
        create_phone_mast(override_tenant='third tenant')
        expected = {
            'tenant_name': 1,
            'second tenant': 1,
            'third tenant': 1,
        }

        result = get_mast_dict()
        self.assertEqual(result, expected)

    def test_get_mast_dict_single_mast_many_tenants(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2')
        create_phone_mast(override_property_name='property 3')
        create_phone_mast(override_property_name='property 4')
        expected = {
            'tenant_name': 4,
        }

        result = get_mast_dict()
        self.assertEqual(result, expected)

    def test_get_mast_dict_many_masts_per_tenant(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2')
        create_phone_mast(override_property_name='property 3')
        create_phone_mast(override_property_name='property 4')

        create_phone_mast(override_tenant='second tenant', override_property_name='property 2')
        create_phone_mast(override_tenant='second tenant', override_property_name='property 3')
        create_phone_mast(override_tenant='second tenant', override_property_name='property 4')

        expected = {
            'tenant_name': 4,
            'second tenant': 3,
        }

        result = get_mast_dict()
        self.assertEqual(result, expected)

    def test_get_sorted_data_by_rent_no_mast(self):
        ascending = 1
        result = get_sorted_data_by_rent(ascending)
        self.assertQuerysetEqual(result, [])

    def test_get_sorted_data_by_rent_one_mast(self):
        create_phone_mast()
        ascending = 1
        expected = ['<PhoneMasts: property_name>']

        result = get_sorted_data_by_rent(ascending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_two_masts_asc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=300)
        ascending = 1
        expected = ['<PhoneMasts: property_name>', '<PhoneMasts: property 2>']

        result = get_sorted_data_by_rent(ascending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_two_masts_desc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=300)
        descending = -1
        expected = ['<PhoneMasts: property 2>', '<PhoneMasts: property_name>']

        result = get_sorted_data_by_rent(descending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_five_masts_desc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=1200)

        create_phone_mast(override_property_name='property 3',
                          override_current_rent=1600)

        create_phone_mast(override_property_name='property 4',
                          override_current_rent=100)

        create_phone_mast(override_property_name='property 5',
                          override_current_rent=5)

        descending = -1
        expected = [
            '<PhoneMasts: property 3>',
            '<PhoneMasts: property 2>',
            '<PhoneMasts: property_name>',
            '<PhoneMasts: property 4>',
            '<PhoneMasts: property 5>',
            ]

        result = get_sorted_data_by_rent(descending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_five_masts_asc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=1200)

        create_phone_mast(override_property_name='property 3',
                          override_current_rent=1600)

        create_phone_mast(override_property_name='property 4',
                          override_current_rent=100)

        create_phone_mast(override_property_name='property 5',
                          override_current_rent=5)

        ascending = 1
        expected = [
            '<PhoneMasts: property 5>',
            '<PhoneMasts: property 4>',
            '<PhoneMasts: property_name>',
            '<PhoneMasts: property 2>',
            '<PhoneMasts: property 3>',
            ]

        result = get_sorted_data_by_rent(ascending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_limited_masts_desc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=1200)

        create_phone_mast(override_property_name='property 3',
                          override_current_rent=1600)

        create_phone_mast(override_property_name='property 4',
                          override_current_rent=100)

        create_phone_mast(override_property_name='property 5',
                          override_current_rent=5)

        create_phone_mast(override_property_name='property 6',
                          override_current_rent=130000)

        create_phone_mast(override_property_name='property 7',
                          override_current_rent=5500)

        create_phone_mast(override_property_name='property 8',
                          override_current_rent=30)

        descending = -1
        expected = [
            '<PhoneMasts: property 6>',
            '<PhoneMasts: property 7>',
            '<PhoneMasts: property 3>',
            '<PhoneMasts: property 2>',
            '<PhoneMasts: property_name>',
            ]

        result = get_sorted_data_by_rent(descending)
        self.assertQuerysetEqual(result, expected)

    def test_get_sorted_data_by_rent_limited_masts_asc(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2',
                          override_current_rent=1200)

        create_phone_mast(override_property_name='property 3',
                          override_current_rent=1600)

        create_phone_mast(override_property_name='property 4',
                          override_current_rent=100)

        create_phone_mast(override_property_name='property 5',
                          override_current_rent=5)

        create_phone_mast(override_property_name='property 6',
                          override_current_rent=130000)

        create_phone_mast(override_property_name='property 7',
                          override_current_rent=5500)

        create_phone_mast(override_property_name='property 8',
                          override_current_rent=30)

        ascending = 1
        expected = [
            '<PhoneMasts: property 5>',
            '<PhoneMasts: property 8>',
            '<PhoneMasts: property 4>',
            '<PhoneMasts: property_name>',
            '<PhoneMasts: property 2>',
            ]

        result = get_sorted_data_by_rent(ascending)
        self.assertQuerysetEqual(result, expected)



