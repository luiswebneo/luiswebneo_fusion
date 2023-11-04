from django.views.generic import TemplateView

from .models import Servico, Funcionario

class IndexView(TemplateView):
  template_name = 'index.html'


class TesteView(TemplateView):
  template_name = '404.html'

class TesteView(TemplateView):
  template_name = '500.html'
