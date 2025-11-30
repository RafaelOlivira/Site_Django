from django.urls import path
from .views import InicioView,LoginView

urlpatterns = [
    path("",LoginView.as_view(), name="login"),
    path("inicio/",InicioView.as_view(), name='inicio'),
]
