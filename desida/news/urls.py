from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.DateilView_1.as_view(), name='news-detail'),
    path('<int:pk>/update', views.UpdatelView_1.as_view(), name='news-update'),
    path('<int:pk>/delete', views.DeleteView_1.as_view(), name='news-delete')
] 