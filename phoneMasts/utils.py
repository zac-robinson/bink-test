from .models import PhoneMasts


def get_mast_dict():
    result_dict = {}
    unique_tenants = PhoneMasts.objects.all().values_list('tenant_name', flat=True).distinct()

    for tenant in unique_tenants:
        number_of_masts = PhoneMasts.objects.filter(tenant_name__exact=tenant).count()
        result_dict[tenant] = number_of_masts

    return result_dict


def get_sorted_data_by_rent(order):
    sort_value = '-current_rent'
    if order > 0:
        sort_value = 'current_rent'
    return PhoneMasts.objects.order_by(sort_value)[:5]
