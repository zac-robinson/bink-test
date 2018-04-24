from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UploadFileForm, ManualUploadForm
from .handle_upload import handle_file_upload, handle_manual_upload

from .models import PhoneMasts

order = 1


def index(request):
    return render_list(request)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_file_upload(request.FILES['my_file'])
            messages.add_message(request, messages.SUCCESS,
                                "Success! File uploaded!",
                                extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse('phoneMasts:index'))
        else:
            messages.add_message(request, messages.ERROR,
                                "File fail to upload",
                                extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('phoneMasts:index'))
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'phoneMasts/index.html', context)


def manual_upload(request):
    if request.method == 'POST':
        form = ManualUploadForm(request.POST)
        if form.is_valid():
            handle_manual_upload(request.POST)
            messages.add_message(request, messages.SUCCESS,
                                "Success! Data uploaded!",
                                extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse('phoneMasts:index'))
        else:
            messages.add_message(request, messages.ERROR,
                                "Failed to upload data",
                                extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('phoneMasts:index'))
    else:
        form = ManualUploadForm()
    context = {
        'form': form,
    }
    return render(request, 'phoneMasts/manual_upload.html', context)


def sort(request):
    global order
    if request.method == 'GET':
        order = order * -1
        return render_list(request)


def get_data():
    global order
    sort_value = '-current_rent'
    if order > 0:
        sort_value = 'current_rent'
    return PhoneMasts.objects.order_by(sort_value)[:5]


def render_list(request):
    masts_by_lease_amount = get_data()
    num_of_masts = get_mast_dict()
    filtered_mast_dict = {}

    total_rent = 0

    for mast in masts_by_lease_amount:
        total_rent += mast.current_rent
        if filtered_mast_dict.get(mast.tenant_name) is None:
            filtered_mast_dict[mast.tenant_name] = num_of_masts[mast.tenant_name]

    context = {
        'masts_by_lease_amount': masts_by_lease_amount,
        'total_rent': total_rent,
        'filtered_mast_dict': filtered_mast_dict
    }
    return render(request, 'phoneMasts/index.html', context)


def get_mast_dict():
    result_dict = {}
    unique_tenants = PhoneMasts.objects.all().values_list('tenant_name', flat=True).distinct()

    for tenant in unique_tenants:
        number_of_masts = PhoneMasts.objects.filter(tenant_name__exact=tenant).count()
        result_dict[tenant] = number_of_masts

    return result_dict
