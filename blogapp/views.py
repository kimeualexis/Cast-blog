from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from . models import Post, Comment
from . forms import CommentForm, UserForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'image', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-created']
	template_name = 'blogapp/index.html'


def detail(request, post_id):
	form = CommentForm(request.POST or None)
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blogapp/detail.html', {'post': post, 'form': form})


def add_comment(request, post_id):
	form = CommentForm(request.POST or None)
	post = get_object_or_404(Post, pk=post_id)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.user = request.user
		comment.save()
		return render(request, 'blogapp/detail.html', {'post': post})
	form = CommentForm()
	return render(request, 'blogapp/detail.html', {'form': form})


class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'image', 'content']

	def get_success_url(self):
		return reverse('blogapp:index')

	def form_valid(self, form):
		return super().form_valid(form)


class PostDeleteView(DeleteView):
	model = Post
	success_url = '/'


def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				posts = Post.objects.filter(user=request.user)
				context = {
					'posts': posts,
					'message': 'Account Created Successful! '
				}
				return render(request, 'blogapp/index.html', context)
	context = {
		'form': form,
	}
	return render(request, 'blogapp/register.html', context)


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				posts = Post.objects.filter(user=request.user)
				context = {
					'posts': posts
				}
				return render(request, 'blogapp/index.html', context)
	return render(request, 'blogapp/login.html')


def logout_user(request):
	logout(request)
	return redirect('blogapp:login')

