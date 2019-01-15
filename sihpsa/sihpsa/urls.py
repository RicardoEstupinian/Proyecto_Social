"""sihpsa URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from sihpsa.views import base
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('miembro/', include(('apps.miembro.urls', 'miembro'), namespace='miembro')),
    path('', base, name="base"),
    path('accounts/login/', login, {'template_name':'login/login.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('modulo-financiero/',include('apps.transaccion.urls')),
    path('venta/', include('apps.ventas.urls')),
    path('inventario/',include(('apps.venta.urls','venta'),namespace='inventario_url')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)