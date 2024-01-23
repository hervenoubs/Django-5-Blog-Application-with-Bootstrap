from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from blog.forms import WritePostForm, SearchForm, NewsletterForm
from blog.models import Category, Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def create_post(request):

    if request.method == "POST":
        postForm = WritePostForm(request.POST, request.FILES)
        if postForm.is_valid():
            post = Post(
                post_title = postForm.cleaned_data['post_title'],
                post_intro = postForm.cleaned_data['post_intro'],
                post_content = postForm.cleaned_data['post_content'],
                post_banner = postForm.cleaned_data['post_banner'],
            )
            post.author = request.user
            post.save()

            categories = postForm.cleaned_data['categories']
            post.categories.set(categories)
            # Set a success message
            messages.success(request, 'Your blog article was successfully submitted and is under review!')
            return redirect('create_post')
    else:
        postForm = WritePostForm()

    category = Category.objects.all()
    srchform = SearchForm()
    nlform = NewsletterForm()
    context = {
        "categories": category,
        "srchform": srchform,
        "nlform": nlform,
        "postForm": postForm,
    }
    return render(request, "accounts/create.html", context)

@login_required
def manage_posts(request):
    posts_with_categories = Post.objects.filter(author=request.user).prefetch_related('categories').all()
    category = Category.objects.all()
    srchform = SearchForm()
    nlform = NewsletterForm()
    context = {
        "categories": category,
        "srchform": srchform,
        "nlform": nlform,
        "posts_with_categories": posts_with_categories,
    }
    return render(request, "accounts/posts.html", context)

@login_required
def edit_post(request, pk):
    # fetch the post along with its related categories
    post = get_object_or_404(Post.objects.prefetch_related('categories'), pk=pk)
    category = Category.objects.all()
    srchform = SearchForm()
    nlform = NewsletterForm()
    context = {
        "categories": category,
        "srchform": srchform,
        "nlform": nlform,
        "post": post,
    }
    return render(request, "accounts/edit-post.html", context)

@login_required
def update_post(request, pk):
    # post = get_object_or_404(Post.objects.prefetch_related('categories'), pk=pk)
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = WritePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.categories.set(form.cleaned_data['categories'])
            post.save()
            return redirect('edit_post', pk=post.pk)
    else:
        form = WritePostForm(instance=post)

    category = Category.objects.all()
    srchform = SearchForm()
    nlform = NewsletterForm()
    context = {
        "categories": category,
        "srchform": srchform,
        "nlform": nlform,
        "post": post,
        "form": form,
    }
    return render(request, "manage_posts", context)

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('manage_posts')

    # If it's a GET request, return a method not allowed response
    return HttpResponseNotAllowed(['POST'])