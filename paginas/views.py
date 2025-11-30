from django.views.generic import TemplateView

# Create your views here.
class InicioView(TemplateView):
    template_name = "paginas/inicio.html"

class LoginView(TemplateView):
    template_name = "paginas/modelo.html"