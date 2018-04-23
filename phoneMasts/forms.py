from django import forms


class UploadFileForm(forms.Form):
    my_file = forms.FileField()


class ManualUploadForm(forms.Form):
    property_name = forms.CharField(max_length=150)
    property_address_1 = forms.CharField(max_length=150)
    property_address_2 = forms.CharField(max_length=150)
    property_address_3 = forms.CharField(max_length=150)
    property_address_4 = forms.CharField(max_length=150)
    unit_name = forms.CharField(max_length=150)
    tenant_name = forms.CharField(max_length=150)
    lease_start_date = forms.CharField(max_length=25)
    lease_end_date = forms.CharField(max_length=25)
    lease_years = forms.IntegerField()
    current_rent = forms.DecimalField(max_digits=10, decimal_places=2)
