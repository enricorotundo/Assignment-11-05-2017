from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from single_page_todo import views

# generate URLs for the views
router = DefaultRouter()
router.register(prefix='todos', viewset=views.TodoViewSet)

# exposes URLs for API and for static files (front-end)
urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

