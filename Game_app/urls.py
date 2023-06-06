from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.root),
    path('destroy_session', views.destroy_session),
    path('guessing', views.guessing),
]