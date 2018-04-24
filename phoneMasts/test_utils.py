from django.test import TestCase
from .utils import *


def create_phone_mast(override='tenant_name', override_property_name='property_name'):

    return PhoneMasts.objects.create(
        property_name=override_property_name,
        property_address_1='property_address_1',
        property_address_2='property_address_2',
        property_address_3='property_address_3',
        property_address_4='property_address_4',
        unit_name='unit_name',
        tenant_name=override,
        lease_start_date='lease_start_date',
        lease_end_date='lease_end_date',
        lease_years='lease_years',
        current_rent='current_rent'
    )


class UtilsTest(TestCase):

    def test_get_mast_dict_no_masts(self):
        result = get_mast_dict()
        self.assertEqual(result, {})

    def test_get_mast_dict_with_mast(self):
        create_phone_mast()
        result = get_mast_dict()
        expected = {
            'tenant_name': 1
        }

        self.assertEqual(result, expected)

    def test_get_mast_dict_single_mast_per_tenant(self):
        create_phone_mast()
        create_phone_mast(override='second tenant')
        create_phone_mast(override='third tenant')

        result = get_mast_dict()

        expected = {
            'tenant_name': 1,
            'second tenant': 1,
            'third tenant': 1,
        }

        self.assertEqual(result, expected)

    def test_get_mast_dict_single_mast_many_tenants(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2')
        create_phone_mast(override_property_name='property 3')
        create_phone_mast(override_property_name='property 4')

        result = get_mast_dict()

        expected = {
            'tenant_name': 4,
        }

        self.assertEqual(result, expected)

    def test_get_mast_dict_many_masts_per_tenant(self):
        create_phone_mast()
        create_phone_mast(override_property_name='property 2')
        create_phone_mast(override_property_name='property 3')
        create_phone_mast(override_property_name='property 4')

        create_phone_mast(override='second tenant', override_property_name='property 2')
        create_phone_mast(override='second tenant', override_property_name='property 3')
        create_phone_mast(override='second tenant', override_property_name='property 4')

        result = get_mast_dict()

        expected = {
            'tenant_name': 4,
            'second tenant': 3,
        }

        self.assertEqual(result, expected)
