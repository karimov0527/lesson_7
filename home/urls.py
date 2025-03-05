from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('smartphones/',include('smartphone.urls'),name='smartphones'),
    # path('laptops/',,name='laptops'),
    # path('aksessuars/',,name='aksessuars'),
    # path('televesions/',,name='televesions'),
]
