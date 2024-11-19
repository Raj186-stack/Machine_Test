from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = router.urls
