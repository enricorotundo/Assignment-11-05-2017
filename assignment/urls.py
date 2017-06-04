from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from single_page_todo import views

router = DefaultRouter()
router.register(prefix='todos', viewset=views.TodoViewSet)

urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

