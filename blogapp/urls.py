from django.urls import path
from . views import PostListView, PostUpdateView, PostDeleteView, PostCreateView
from . import views

app_name = 'blogapp'

urlpatterns = [
	path('', PostListView.as_view(), name='index'),
	path('myposts/', views.my_posts, name='myposts'),
	path('add_post/', PostCreateView.as_view(), name='add_post'),
	path('(?P<post_id>[0-9]+)/', views.detail, name='detail'),
	path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
	path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
	path('(?P<post_id>[0-9]+)/comment/', views.add_comment, name='comment'),
	path('register/', views.register, name='register'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
]