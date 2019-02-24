from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . models import Post, Comment


# Create your views here.
class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-created']
	template_name = 'blogapp/index.html'


class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'blogapp/detail.html'


class CommentCreateView(CreateView):
	model = Comment
	fields = ['comment']
	template_name = 'blogapp/detail.html'

	def form_valid(self, form, **kwargs):
		post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
		form.instance.post = post
		return super(CommentCreateView, self).form_valid(form)
