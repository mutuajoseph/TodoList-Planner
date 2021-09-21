from rest_framework import routers, urlpatterns
from .api import TodoViewSet

# create an instance of the router
router = routers.DefaultRouter()
router.register('api/todos', TodoViewSet, 'todos')

urlpatterns = router.urls