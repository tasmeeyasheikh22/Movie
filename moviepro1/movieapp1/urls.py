from django.urls import path

from .views import *

urlpatterns=[
    path("av/",addview),
    path("sv/",viewsview),
    path("uv/<int:id>/",updateview),
    path("dv/<int:ud>",deleteview)
]
