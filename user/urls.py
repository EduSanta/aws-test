from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('list', views.get_user_list),
    path('add', views.add_user)
]

urlpatterns += router.urls
