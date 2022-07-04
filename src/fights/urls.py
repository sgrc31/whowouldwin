from django.urls import path
from django.views.generic import RedirectView

from .views import HomePageView, FightDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('fights/', RedirectView.as_view(pattern_name='home'),
         name='fights_list'),
    path('fights/<slug:suuid>/', FightDetailView.as_view(), name='fight_detail'),
    ]
