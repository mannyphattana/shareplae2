from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('words/', views.WordListView.as_view(), name='words'),
    path('search/', views.search_detail, name='search-detail'),
    path('word/<int:pk>',views.word_detail,name='word-detail'),
    path('favorite/<int:pk>',views.favorite,name='favorite'),
    path('unfavorite/<int:pk>',views.unfavorite,name='unfavorite'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('MyFavorites/', views.myfavorites, name='myfavorites'),
    path('createcrud/', views.create_crud, name='createcrud'),
    path('listcrud/', views.list_crud, name='listcrud'),
    path('update/<int:pk>/', views.update_crud, name='updatecrud'),
    path('delete/<int:pk>/', views.delete_crud, name='deletecrud'),
    path('deletecomment/<int:pk>/', views.delete_comment, name='deletecomment'),
    path('admindeletecomment/', views.admin_delete_comment, name='admindeletecomment'),
]
