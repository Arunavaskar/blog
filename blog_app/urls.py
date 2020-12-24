from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView
# home_view
from . import views

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', HomeView.as_view(), name='home_view'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    # path('test/', views.home_view, name='test'),
    # path('test/', home_view.as_view(), name='test'),
    path('articles/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('articles/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
