from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    """
    Default home route.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mercedec Home'
        return context