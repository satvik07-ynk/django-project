from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('measurement_iv', views.measurement_iv, name='measurement_iv'),
    path('measurement_stransient', views.measurement_stransient, name='measurement_stransient'),
    path('measurement_otransient', views.measurement_otransient, name='measurement_otransient'),
    path('run_transient_measurement', views.run_transient_measurement, name="run_transient_measurement"),
]

htmx_urlpatterns = [
    path('hx_parameters', views.hx_parameters, name='hx_parameters'),
]

urlpatterns += htmx_urlpatterns