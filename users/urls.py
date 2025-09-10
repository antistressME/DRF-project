from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentViewSet, UserCreateAPIView, UserDestroyAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentViewSet)


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete_user"),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
urlpatterns += router.urls
