import os

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "example/web/home.html"
    extra_context = {"vars": os.environ.items()}
