from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Smartphoneslist.as_view(),name='smartphone_list'),
    path('smartphone/<int:pk>',smartphone_det,name = 'smartphone_det'),
    path('smartphone_create/',create_smartphone,name='smartphone_create'),
    path('smartphone_update/<int:pk>',update_smartphone,name='smartphone_update'),
    path('smartphone_delete/<int:pk>',delete_smartphone,name='smartphone_delete')
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)