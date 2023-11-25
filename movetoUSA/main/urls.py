


from django.urls import path, re_path
from .views import *

urlpatterns=[
    path('', index, name='home'),
    path('states/', StatesMain.as_view(), name='states_main'),
    path('states/<slug:state_slug>/', show_states, name='states'),
    path('category/<int:cat_id>/', show_category, name='category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('login/', login, name='login'),
]