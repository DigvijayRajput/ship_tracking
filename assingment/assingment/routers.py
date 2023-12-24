"""
Routers provide a convenient and consistent way of automatically
determining the URL conf for your API.
They are used by simply instantiating a Router class, and then registering
all the required ViewSets with that router.
For example, you might have a `urls.py` that looks something like this:
    router = routers.DefaultRouter()
    router.register('users', UserViewSet, 'user')
    router.register('accounts', AccountViewSet, 'account')
    urlpatterns = router.urls
"""
from rest_framework import routers
from ship import views as ship_views



router = routers.DefaultRouter()

router.register(r'ships', ship_views.ShipViewSet)
router.register(r'positions', ship_views.ShipPositionViewSet)

