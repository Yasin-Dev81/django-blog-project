from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import generic

from .models import BlogPost
from .forms import NewOrUpdateBlogPostForm


# blog list functional view
def blog_list_response(request):  # only pub
    blog_list = BlogPost.objects.filter(status='pub').order_by('-datetime_edited')
    return render(request, 'blog/blog_list.html', context={'blogs_list': blog_list})


# blog list class-based view
class PostListView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-datetime_edited')


# blog detail functional view
def blog_detail_response(request, pk):
    blog_target = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', context={'blog': blog_target})


# blog detail class-based view
class BlogDetailView(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    model = BlogPost
    context_object_name = 'blog'


# add blog functional view
def add_blog_response(request):
    print('method:', request.method)
    if request.method == 'POST':
        blogpost_form = NewOrUpdateBlogPostForm(request.POST)
        if blogpost_form.is_valid():
            blogpost_form.save()
            return redirect('blog_list_url')
        else:
            blogpost_form = NewOrUpdateBlogPostForm()
    else:
        blogpost_form = NewOrUpdateBlogPostForm()
    return render(request, 'blog/add_blog.html', context={'form': blogpost_form, 'page_title': 'AddNewBlog'})


# add blog class-based view
class AddBlogView(generic.CreateView):
    form_class = NewOrUpdateBlogPostForm
    template_name = 'blog/add_blog.html'


# update blog functional view
def update_blog_response(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    print('blog post:', blog_post)
    blogpost_form = NewOrUpdateBlogPostForm(request.POST or None, instance=blog_post)
    if blogpost_form.is_valid():
        blogpost_form.save()
        return redirect('blog_detail_url', blog_post.pk, blog_post.title)
    else:
        blogpost_form = NewOrUpdateBlogPostForm(request.POST or None, instance=blog_post)
    return render(request, 'blog/add_blog.html', context={'form': blogpost_form, 'page_title': 'UpdateBlog'})


# update blog class-based view
class UpdateBlogView(generic.UpdateView):
    form_class = NewOrUpdateBlogPostForm
    template_name = 'blog/add_blog.html'
    model = BlogPost


# delete blog functional view
def delete_blog_response(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list_url')
    return render(request, 'blog/blog_delete.html', context={'blog_post': blog_post})


# delete blog class-based view
class DeleteBlogView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/blog_delete.html'
    # success_url = '/blog/'

    def get_success_url(self):
        return reverse('blog_list_url')
