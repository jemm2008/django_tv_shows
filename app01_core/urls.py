from django.urls import path
from . import views
urlpatterns = [
    path('', views.shows),
    path('shows/', views.shows),
    path('shows/<int:id_solicitado>', views.showid),
    path('shows/<int:id_solicitado>/edit', views.showedit),
    path('shows/<int:id_solicitado>/delete', views.showdelete),
    path('shows/new', views.newshow)
]
