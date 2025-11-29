from django.urls import path
from .views import SobreView,PrincipalView

urlpatterns = [
    path("",PrincipalView.as_view(), name="inicio"),
    path("sobre/",SobreView.as_view(), name='sobre'),
]
