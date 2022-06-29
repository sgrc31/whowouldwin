from django.views.generic import ListView
from .models import Fight


class HomePageView(ListView):
    template_name = 'home.html'
    model = Fight
    context_object_name = 'active_fights_list'
