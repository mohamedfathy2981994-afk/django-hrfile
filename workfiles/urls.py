from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import MaindataListView, MaindataDetailView, home,generate_html
from workfiles import views


urlpatterns = [
    path('', views.home, name='home'),
    path('workfile/', MaindataListView.as_view(), name='maindata-list'),
    path('workfile/<int:pk>/', MaindataDetailView.as_view(), name='maindata-detail'),
    path('generate_html/<int:pk>/', generate_html, name='generate_html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)