from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AminoreaderView

router = DefaultRouter()
router.register('aminoreader', AminoreaderView)

urlpatterns = [
    path('aminoreader/', include(router.urls)),
]
