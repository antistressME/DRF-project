from rest_framework.routers import SimpleRouter

from subs.apps import SubsConfig
from subs.views import SubscriptionViewSet

app_name = SubsConfig.name

router = SimpleRouter()
router.register("", SubscriptionViewSet)


urlpatterns = []
urlpatterns += router.urls
