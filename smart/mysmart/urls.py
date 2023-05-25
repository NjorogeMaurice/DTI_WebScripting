
from rest_framework import routers
from mysmart.views import getScripts
router = routers.DefaultRouter()
router.register(r'data',getScripts)

urlpatterns = router.urls