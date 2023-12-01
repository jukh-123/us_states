


from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "4_digit_year")

urlpatterns=[
    path('', views.index, name='home'),
    path('states/', views.StatesMain.as_view(), name='states_main'),
    path('states/<slug:state_slug>/', views.show_states, name='states'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('map/', views.show_map, name='map_page'),
    path('archive/<4_digit_year:year>', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('add_page/', views.add_page, name='add_page'),
    path('login/', views.login, name='login'),
]