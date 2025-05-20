from ninja import Router
from typing import List
from .schemas import WaitlistListEntrySchema, WaitlistDetailEntrySchema, WaitlistCreateEntrySchema
from .models import WaitlistEntry
from django.shortcuts import get_object_or_404

from ninja_jwt.authentication import JWTAuth
router = Router()


@router.get("", response=List[WaitlistListEntrySchema], auth=JWTAuth())
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs


@router.get("{entry_id}/", response=WaitlistDetailEntrySchema, auth=JWTAuth())
def get_waitlist_entry(request, entry_id: int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj


@router.post("", auth=JWTAuth())
def add_to_waitlist(request, data: WaitlistCreateEntrySchema):
    entry = WaitlistEntry.objects.create(user=request.user, **data.dict())
    return {"message": "Dodano do listy oczekujących", "id": entry.id}
