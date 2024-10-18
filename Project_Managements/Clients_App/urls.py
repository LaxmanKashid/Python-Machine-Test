from django.urls import path
from .views import ClientList, ClientDetail, ProjectCreate, UserProjectList

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreate.as_view(), name='project-create'),
    path('projects/', UserProjectList.as_view(), name='user-projects'),
]

