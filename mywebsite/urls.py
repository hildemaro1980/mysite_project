"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
### For translations ###############
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

### End for translations ########################

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('rosetta/',include('rosetta.urls')),
#    path('', views.home),
#    #path('test',views.test),
#    path('myhome',views.test),
#    path('blog/', include('blog.urls')),
#]
urlpatterns = i18n_patterns(
    path('startpage',views.startPage),
    path(_('admin/'), admin.site.urls),
    path('rosetta/',include('rosetta.urls')),
    #path('', views.home),
    #path('test',views.test),
    path('',views.test),
    path('blog/', include('blog.urls')),
 )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)