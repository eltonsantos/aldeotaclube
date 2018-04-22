"""aldeotaclube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from noticias import urls as noticias_urls
from atletas import urls as atletas_urls
from artilharia import urls as artilharia_urls
from jogos import urls as jogos_urls
from .views import sobre, contato
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(home_urls)),
    path('sobre/', sobre, name='sobre'),
    path('noticias/', include(noticias_urls)),
    path('atletas/', include(atletas_urls)),
    path('artilharia/', include(artilharia_urls)),
    path('jogos/', include(jogos_urls)),
    path('contato/', contato, name='contato'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
