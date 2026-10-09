from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from accounts.permissions import consultant_required

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import Http404 

from .utils import all_requests, ALL_REQUEST_MODELS
# Create your views here.


@login_required
@consultant_required
def home(request):
    return render(request, "home.html", {
        "requests": all_requests()
    })


def request_detail(request, ct_id, pk):
    content_type = get_object_or_404(ContentType, pk=ct_id)
    model = content_type.model_class()

    if model is None:
        raise Http404

    if model not in ALL_REQUEST_MODELS:
        raise Http404

    obj = get_object_or_404(model, pk=pk)

    return render(request, "request_detail.html", {
        "obj":obj, "ct_id":ct_id, 
    })