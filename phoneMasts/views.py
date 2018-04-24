from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UploadFileForm, ManualUploadForm
from .handle_upload import handle_file_upload, handle_manual_upload
from .utils import *
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

    return render(request, 'phoneMasts/index.html')


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

    return render(request, 'phoneMasts/manual_upload.html')


def sort(request):
    global order
    if request.method == 'GET':
        order = order * -1
        return render_list(request)


def render_list(request):
    masts_by_lease_amount = get_sorted_data_by_rent(order)
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
