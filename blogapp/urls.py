from django.urls import path
from . views import PostListView, PostDetailView, CommentCreateView

app_name = 'blogapp'

urlpatterns = [
	path('', PostListView.as_view(), name='index'),
	path('<int:pk>/', PostDetailView.as_view(), name='detail'),
	path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]