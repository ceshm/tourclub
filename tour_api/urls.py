from rest_framework import routers
from tour_api.views import TourViewSet, TeamViewSet

router = routers.DefaultRouter()

router.register('/tours', TourViewSet, basename="tour")
router.register('/teams', TeamViewSet, basename="team")
