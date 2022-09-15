from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]
from django.urls import path, include

urlpatterns = [
    path('osoby/', include('osoby.urls')),
    path('admin/', admin.site.urls),
]