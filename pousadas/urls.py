from django.urls import path

from pousadas import views

app_name = 'pousadas'

urlpatterns = [
    path('', views.PousadaList.as_view(), name='list'),
    path('create/', views.PousadaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.PousadaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.PousadaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PousadaDelete.as_view(), name='delete')
]