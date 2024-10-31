from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage, name='homepage'),
    path('polling-unit',views.polling_unit,name='polling_unit'),
    path('lga', views.lga, name='lga'),
    path('store-election-result', views.store_election_result, name='store_election_result')

]