from ninja import Schema
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from users.api import router as users_router

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlist/", "waitlist.api.router")
api.add_router("/announcements/", "announcements.api.router")
api.add_router("/auth/", users_router)


class UserSchema(Schema):
    name: str = None
    username: str
    is_authenticated: bool
    # if not request.user.is_authenticated
    email: str = None


@api.get("/me", response=UserSchema, auth=JWTAuth())
def me(request):
    return request.user


@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello from Django Ninja!"}
