

from django.urls import include, path
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from .views import ItemsPage,OrderAdd

router = SimpleRouter()
router.register("api/items",ItemsPage)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/order-add/",OrderAdd.as_view())

] + router.urls
