import pytest
from django.urls import reverse, resolve
from fights.models import Fighter


class TestHomepage:
    def test_homepage_path(self):
        path = resolve('/')
        assert path.route == ''

    def test_homepage_url_name(self):
        path = resolve('/')
        assert path.url_name == 'home'

    @pytest.mark.django_db
    def test_homepage_existence(self, client):
        response = client.get(reverse('home'))
        assert response.status_code == 200
        assert response.template_name[0] == 'home.html'


class TestFighterModel:
    @pytest.mark.django_db
    def test_fighter_count(self):
        assert Fighter.objects.count() == 0

    @pytest.mark.django_db
    def test_fighter_create(self):
        Fighter.objects.create(name="Tizio",
                               description="descrizione tizio",
                               powers="poteri tizio")
        assert Fighter.objects.count() == 1
        test_fighter_1 = Fighter.objects.get(id=1)
        assert test_fighter_1.name == "Tizio"
