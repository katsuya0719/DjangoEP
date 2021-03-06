"""EnergyPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from heatBalance import views
from project.views import model_form_upload,ListView,DetailView

router=routers.DefaultRouter()
router.register(r'heat',views.heatBalViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^project/$',ListView.as_view(),name='project'),
    url(r'^upload/$',model_form_upload,name='upload'),
    url(r'^project/(?P<pk>\d+)/$',DetailView.as_view(),name='detail'),
]
