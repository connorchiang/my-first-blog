from django.shortcuts import render
from django.utils import timezone
from .models import Post,Cv
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,CvForm
from django.shortcuts import redirect



# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	cvs = Cv.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts,'cvs': cvs})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})



# Create your views here.


def cv_detail(request,pk):
	cv = get_object_or_404(Cv, pk=pk)
	return render(request, 'blog/cv_detail.html', {'cv': cv})


def cv_edit(request, pk):
	cv = get_object_or_404(Cv, pk=pk)
	if request.method == "POST":
		form = CvForm(request.POST, instance=cv)
		if form.is_valid():
			cv = form.save(commit=False)
			cv.published_date = timezone.now()
			cv.save()
			return redirect('cv_detail', pk=cv.pk)
	else:
		form = CvForm(instance=cv)
	return render(request, 'blog/cv_edit.html', {'form': form})