import pytest
from django.urls import reverse, resolve


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
