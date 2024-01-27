

from django.urls import include, path
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from .views import ItemsPage

router = SimpleRouter()
router.register("api/items",ItemsPage)

urlpatterns = [
    path("admin/", admin.site.urls),


] + router.urls
