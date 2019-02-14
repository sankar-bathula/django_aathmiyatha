from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 
from aathmiyatha.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index_home(request):
	context ={'Home' : 'Home Amf'}
	return render(request, 'aathmiyatha/index.html', context)
def home(request):
	context = {'posts':Post.objects.all()}
	return render(request, 'aathmiyatha/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'aathmiyatha/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	# ordering = ['-date_posted'] #change the order latest post add '-'
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'aathmiyatha/user_posts.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #change the order latest post add '-'
	paginate_by = 5
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		"""This method is implemented for to give user id to author """
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		"""This method is implemented for to give user id to author """
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		"""This is implemeted for to allow update particular users related posts only"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		"""This is implemeted for to allow update particular users related posts only"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'aathmiyatha/about.html', {'title':'About'})

