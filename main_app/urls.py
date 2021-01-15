from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('about/', views.about, name="about"),
   path('sounds/', views.sounds_show, name="sounds_show"),
   path('sounds/create/', views.SoundCreate.as_view(), name="sounds_create"),
   path('sounds/<int:pk>/update/', views.SoundUpdate.as_view(), name="sounds_update"),
   path('sounds/<int:pk>/delete/', views.SoundDelete.as_view(), name="sounds_delete")
]

