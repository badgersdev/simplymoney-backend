from ninja import Router
from ninja_jwt.tokens import RefreshToken
from django.http import JsonResponse
from .schemas import UserSignupSchema
from .models import CustomUser

router = Router()


@router.post("/signup")
def register_user(request, data: UserSignupSchema):
    print("DOSTAŁEM DANE:", data)

    if CustomUser.objects.filter(email=data.email).exists():
        return JsonResponse({"message": "Email already exists."}, status=400)

    user = CustomUser.objects.create_user(
        email=data.email,
        password=data.password,
    )

    # auto login
    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        "message": "Account created successfully.",
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }, status=201)
