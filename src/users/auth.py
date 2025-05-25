from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import UntypedToken
from django.contrib.auth import get_user_model
from django.conf import settings
from jwt import decode as jwt_decode, InvalidTokenError


class JWTAuthFromCookie(JWTAuth):
    def authenticate(self, request, token=None):
        token = request.COOKIES.get("auth-token")
        if not token:
            return None

        try:
            UntypedToken(token)
            decoded = jwt_decode(
                token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded.get("user_id")

            if not user_id:
                return None

            user = get_user_model().objects.get(id=user_id)
            return user

        except (InvalidTokenError, get_user_model().DoesNotExist, KeyError):
            return None
