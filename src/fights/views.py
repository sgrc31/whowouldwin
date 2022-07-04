from django.views.generic import ListView, DetailView
from .models import Fight


class HomePageView(ListView):
    template_name = 'home.html'
    model = Fight
    context_object_name = 'active_fights_list'


class FightDetailView(DetailView):
    template_name = 'fight_detail.html'
    model = Fight
    slug_field = 'small_uuid'
    slug_url_kwarg = 'suuid'
