from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.permissions import consultant_required

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import Http404 
from django.utils import timezone

from .utils import all_requests, ALL_REQUEST_MODELS, create_filing_from_request
from .models import ConsultantRequest, Filing
from .forms import FILING_FORM_MAP
# Create your views here.


@login_required
@consultant_required
def home(request):
    return render(request, "consultant_home.html", {
        "requests": all_requests()
    })

@login_required
@consultant_required
def request_detail(request, ct_id, pk):
    content_type = get_object_or_404(ContentType, pk=ct_id)
    model = content_type.model_class()

    if model is None:
        raise Http404

    if model not in ALL_REQUEST_MODELS:
        raise Http404

    obj = get_object_or_404(model, pk=pk)

    if obj.user_type in ("seller", "landlord"):
        has_taken = Filing.objects.filter(
        consultant=request.user,
        source_request_ct=content_type,
        source_request_id=obj.pk,
        ).exists()

    else:
        has_taken = ConsultantRequest.objects.filter(
        consultant=request.user,
        content_type=content_type,
        object_id=obj.pk,
        ).exists()

    return render(request, "request_detail.html", {
        "obj":obj, "ct_id":ct_id, "has_taken":has_taken 
    })


@login_required
@consultant_required
@require_POST
def take_request(request, ct_id, pk):
    content_type = get_object_or_404(ContentType, pk=ct_id)
    model = content_type.model_class()

    if model is None:
        raise Http404
    
    if model not in ALL_REQUEST_MODELS:
        raise Http404
    
    req = get_object_or_404(model, pk=pk)

    if req.user_type in ("buyer", "tenant"): 
        ConsultantRequest.objects.get_or_create(
            consultant=request.user,
            content_type=content_type,
            object_id=req.pk
        )

    if req.user_type in ("seller", "landlord"):
        create_filing_from_request(req, request.user)

    return redirect("consultants:request_detail", ct_id=ct_id, pk=pk)


@login_required
@consultant_required
def dashboard(request):
    taken_requests = ConsultantRequest.objects.filter(
        consultant=request.user,
    ).select_related("content_type")

    draft_filings = Filing.objects.filter(
        consultant=request.user,
        is_published=False
    ).order_by("-created_at")

    published_filings = Filing.objects.filter(
        consultant=request.user,
        is_published=True
    ).order_by("-created_at")

    return render(request, "dashboard.html", {
        "takes":taken_requests,
        "draft_filings":draft_filings,
        "published_filings":published_filings
    })


@login_required
@consultant_required
def filing_edit(request, pk):  
    filing = get_object_or_404(Filing, pk=pk, consultant=request.user)
    request_owner = filing.source_request.user

    form_class = FILING_FORM_MAP[(filing.property_type, filing.listing_type)]

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=filing)

        if form.is_valid():
            form.save()

            return redirect("consultants:dashboard")

    else:
        form = form_class(instance=filing)

    return render(request, "filing_edit.html", {"form":form, "filing":filing, "request_owner":request_owner})


@login_required
@consultant_required
@require_POST
def delete_request(request, ct_id, pk):
    content_type = get_object_or_404(ContentType, pk=ct_id)

    take = get_object_or_404(
        ConsultantRequest,
        consultant=request.user,
        content_type=content_type,
        object_id=pk
    )
    take.delete()

    return redirect("consultants:dashboard")


@login_required
@consultant_required
@require_POST
def delete_filing(request, pk):
    filing = get_object_or_404(Filing, pk=pk, consultant=request.user)
    filing.delete()

    return redirect("consultants:dashboard")


@login_required
@consultant_required
@require_POST
def publish_filing(request, pk):
    filing = get_object_or_404(Filing, pk=pk, consultant=request.user)
    filing.is_published = True
    filing.published_at = timezone.now()
    filing.save()

    return redirect("consultants:dashboard")


@login_required
@consultant_required
@require_POST
def unpublish_filing(request, pk):
    filing = get_object_or_404(Filing, pk=pk, consultant=request.user)
    filing.is_published = False
    filing.save()

    return redirect("consultants:dashboard")