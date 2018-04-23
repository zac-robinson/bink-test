import csv
import io

from .models import PhoneMasts


def handle_file_upload(csv_file):
    decoded_file = csv_file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    for line in csv.reader(io_string, dialect="excel"):
        if line[0] != 'Property Name':
            _, created = PhoneMasts.objects.get_or_create(
                property_name=line[0],
                property_address_1=line[1],
                property_address_2=line[2],
                property_address_3=line[3],
                property_address_4=line[4],
                unit_name=line[5],
                tenant_name=line[6],
                lease_start_date=line[7],
                lease_end_date=line[8],
                lease_years=line[9],
                current_rent=line[10],
            )


def handle_manual_upload(entry):
    _, created = PhoneMasts.objects.get_or_create(
        property_name=entry['property_name'],
        property_address_1=entry['property_address_1'],
        property_address_2=entry['property_address_2'],
        property_address_3=entry['property_address_3'],
        property_address_4=entry['property_address_4'],
        unit_name=entry['unit_name'],
        tenant_name=entry['tenant_name'],
        lease_start_date=entry['lease_start_date'],
        lease_end_date=entry['lease_end_date'],
        lease_years=entry['lease_years'],
        current_rent=entry['current_rent'],
    )
