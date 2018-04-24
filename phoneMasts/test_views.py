from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
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


class IndexViewTest(TestCase):

    def test_no_data(self):
        response = self.client.get(reverse('phoneMasts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_rent'], 0)
        self.assertEqual(response.context['filtered_mast_dict'], {})
        self.assertContains(response, "No mast data available.")
        self.assertQuerysetEqual(response.context['masts_by_lease_amount'], [])

    def test_with_single_phone_mast(self):
        expected = {
                'tenant_name': 1
            }

        create_phone_mast()
        response = self.client.get(reverse('phoneMasts:index'))

        self.assertEqual(response.context['total_rent'], 150)
        self.assertEqual(response.context['filtered_mast_dict'], expected)
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: property_name>']
        )

    def test_with_single_phone_mast_rent_two_decimal_places(self):
        expected = {
                'tenant_name': 1
            }

        create_phone_mast(override_current_rent=300.5144)
        response = self.client.get(reverse('phoneMasts:index'))

        self.assertEqual(response.context['total_rent'], Decimal('300.51'))
        self.assertEqual(response.context['filtered_mast_dict'], expected)
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: property_name>']
        )

    def test_with_two_phone_masts(self):
        expected = {
                'tenant_name': 1,
                'zac': 1
            }

        create_phone_mast()
        create_phone_mast(override_tenant='zac',
                          override_property_name='test',
                          override_current_rent=2000)

        response = self.client.get(reverse('phoneMasts:index'))

        self.assertEqual(response.context['total_rent'], 2150)
        self.assertEqual(response.context['filtered_mast_dict'], expected)
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: property_name>', '<PhoneMasts: test>']
        )

    def test_with_five_phone_masts(self):
        expected = {
                'tenant_name': 4,
                'zac': 1
            }

        create_phone_mast()
        create_phone_mast(override_tenant='zac',
                          override_property_name='test',
                          override_current_rent=2000)

        create_phone_mast(override_property_name='test property',
                          override_current_rent=300)

        create_phone_mast(override_property_name='test property 2',
                          override_current_rent=5000)

        create_phone_mast(override_property_name='test property 3',
                          override_current_rent=40)

        response = self.client.get(reverse('phoneMasts:index'))

        self.assertEqual(response.context['total_rent'], 7490)
        self.assertEqual(response.context['filtered_mast_dict'], expected)
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: test property 3>', '<PhoneMasts: property_name>',
             '<PhoneMasts: test property>', '<PhoneMasts: test>',
             '<PhoneMasts: test property 2>'
            ]
        )

    def test_with_more_than_five_phone_masts(self):
        expected = {
                'tenant_name': 7
            }

        create_phone_mast()
        create_phone_mast(override_property_name='test',
                          override_current_rent=2000)

        create_phone_mast(override_property_name='test property',
                          override_current_rent=300)

        create_phone_mast(override_property_name='test property 2',
                          override_current_rent=5000)

        create_phone_mast(override_property_name='test property 3',
                          override_current_rent=40)

        create_phone_mast(override_property_name='test property 4',
                          override_current_rent=75)

        create_phone_mast(override_property_name='test property 5',
                          override_current_rent=1500)

        response = self.client.get(reverse('phoneMasts:index'))

        self.assertEqual(response.context['total_rent'], 2065)
        self.assertEqual(response.context['filtered_mast_dict'], expected)
        self.assertQuerysetEqual(
            response.context['masts_by_lease_amount'],
            ['<PhoneMasts: test property 3>', '<PhoneMasts: test property 4>',
             '<PhoneMasts: property_name>', '<PhoneMasts: test property>',
             '<PhoneMasts: test property 5>'
            ]
        )


class ManualUploadViewTest(TestCase):

    def test_no_data(self):
        response = self.client.get(reverse('phoneMasts:manual_upload'))
        self.assertEqual(response.status_code, 200)
        print(response.context)


# class UploadFileViewTest(TestCase):

#     def test_no_data(self):
#         response = self.client.post(reverse('phoneMasts:upload'))
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No mast data available.")
#         self.assertQuerysetEqual(response.context['masts_by_lease_amount'], [])

#     def test_with_valid_phone_mast(self):
#         create_phone_mast()
#         response = self.client.get(reverse('phoneMasts:upload'))
#         self.assertQuerysetEqual(
#             response.context['masts_by_lease_amount'],
#             ['<PhoneMasts: test property>']
#         )


# class SortViewTest(TestCase):

#     def test_no_data(self):
#         response = self.client.get(reverse('phoneMasts:sort'))
#         self.assertEqual(response.status_code, 200)
#         print(response)
