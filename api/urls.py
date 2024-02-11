from rest_framework import routers 
from .views import PostViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('post', PostViewSet, 'post_api')

urlpatterns = router.urls