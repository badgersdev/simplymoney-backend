from ninja import Router
from ninja_jwt.authentication import JWTAuth
from typing import List, Optional
from django.db import models
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Announcement, AnnouncementImage
from .schemas import AnnouncementDetailEntrySchema, AnnouncementListEntrySchema

router = Router()


@router.get("", response=List[AnnouncementListEntrySchema])
def list_announcements(request, q: Optional[str] = None):
    announcements = Announcement.objects.all()

    if q:
        announcements = announcements.filter(
            models.Q(label__icontains=q)
            | models.Q(description__icontains=q)
            | models.Q(location__icontains=q)
            | models.Q(category__icontains=q)
        )

    return [
        {
            "id": a.id,
            "label": a.label,
            "category": a.category,
            "location": a.location,
            "exchange_type": a.exchange_type,
            "seller_type": a.seller_type,
            "timestamp": a.timestamp,
            "show_email": a.show_email,
            "show_phone": a.show_phone,
            "images": [img.image.url for img in a.images.all()],
        }
        for a in announcements.order_by("-timestamp")
    ]


@router.get("{announcement_id}/", response=AnnouncementDetailEntrySchema)
def get_announcement_detail(request, announcement_id: int):
    obj = get_object_or_404(Announcement, id=announcement_id)
    return {
        "id": obj.id,
        "label": obj.label,
        "description": obj.description,
        "location": obj.location,
        "category": obj.category,
        "exchange_type": obj.exchange_type,
        "seller_type": obj.seller_type,
        "email": obj.email,
        "phone": obj.phone,
        "show_email": obj.show_email,
        "show_phone": obj.show_phone,
        "timestamp": obj.timestamp,
        "updated": obj.updated,
        "images": [img.image.url for img in obj.images.all()],
    }


@router.post("", auth=JWTAuth())
def create_announcement(request):

    # text fields
    label = request.POST.get("label")
    description = request.POST.get("description")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    show_email = request.POST.get("show_email") == "true"
    show_phone = request.POST.get("show_phone") == "true"
    category = request.POST.get("category")
    exchange_type = request.POST.get("exchange_type")
    seller_type = request.POST.get("seller_type")
    location = request.POST.get("location")
    # files
    reqest_images = request.FILES.getlist("images")

    # Image validation
    if not reqest_images or len(reqest_images) == 0:
        return JsonResponse({"message": "Musisz dodać co najmniej 1 zdjęcie."}, status=400)

    if len(reqest_images) > 3:
        return JsonResponse({"message": "Możesz dodać maksymalnie 3 zdjęcia."}, status=400)

    # Create Announcement
    announcement = Announcement.objects.create(
        user=request.user,
        label=label,
        description=description,
        email=email,
        phone=phone,
        show_email=show_email,
        show_phone=show_phone,
        category=category,
        exchange_type=exchange_type,
        seller_type=seller_type,
        location=location,
    )
    # Add Images
    for img in reqest_images:
        AnnouncementImage.objects.create(announcement=announcement, image=img)

    return JsonResponse({"message": "Ogłoszenie dodane!", "id": announcement.id}, status=200)
