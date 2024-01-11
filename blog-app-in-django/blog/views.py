from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comments, Category, Contacts
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.db.models import Count
import random

def blog_index(request):
    posts = Post.objects.annotate(num_comments=Count('comments'))
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category_name):
    category = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(categories=category).order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
        "current_category": category,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                visitor_name = form.cleaned_data["visitor_name"],
                visitor_email = form.cleaned_data["visitor_email"],
                visitor_comment = form.cleaned_data["visitor_comment"],
                post = post,
            )
            comment.save()
            # Set a success message
            messages.success(request, 'Your comment was successfully submitted! We value comments!')

            return redirect('blog_detail', pk=post.pk)
        else:
            return render(request, 'blog_detail', {'form': form})

    comments = Comments.objects.filter(post=post)
    categories = Category.objects.all()
    num_comments = comments.count()

    # get only the first 3 posts randomly for the sidebar posts
    all_posts = list(Post.objects.all())
    random.shuffle(all_posts)
    random_posts = all_posts[:3]

    context = {
        "post": post,
        "comments": comments,
        "categories": categories,
        "random_posts": random_posts,
        "form": CommentForm(),
        "num_comments": num_comments,
    }
    return render(request, "blog/post.html", context)

def about(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, "blog/about.html", context)

def contact(request):
    categories = Category.objects.all()

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contacts = Contacts(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                message = form.cleaned_data['message'],
            )
            contacts.save()
            # Set a success message
            messages.success(request, 'Your message was successfully submitted! We will get back to you as soon as possible.')

            return redirect('contact')
        else:
            return render(request, 'contact', {'form': form})

    context = {
        "categories": categories,
        "form": ContactForm(),
    }

    return render(request, "blog/contact.html", context)

def shop(request):
    return HttpResponse("Shopping page")
