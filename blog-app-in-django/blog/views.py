from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Post, Comments, Category, Contacts, Newsletter
from .forms import CommentForm, ContactForm, NewsletterForm, SearchForm
from django.contrib import messages
from django.db.models import Count
import random

def blog_index(request):

    srchform = SearchForm()
    nlform = NewsletterForm()
    if request.method == "POST":
        nlform = NewsletterForm(request.POST)
        if nlform.is_valid():
            newsletter = Newsletter(
                firstname = nlform.cleaned_data['firstname'],
                email = nlform.cleaned_data['email'],
            )
            newsletter.save()
            # Set a success message
            return JsonResponse({'message': 'Subscribed successfully!'})
        else:
            return JsonResponse({'error': 'Invalid form submission.'}, status=400)
    else:
        nlform = NewsletterForm()

    posts = Post.objects.annotate(num_comments=Count('comments'))
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
        "srchform": srchform,
        "nlform": nlform,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category_name):
    category = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(categories=category).order_by("-created_on")
    categories = Category.objects.all()
    srchform = SearchForm()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
        "current_category": category,
        "srchform": srchform,
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
    srchform = SearchForm()
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
        "srchform": srchform,
    }
    return render(request, "blog/post.html", context)

def about(request):
    categories = Category.objects.all()
    srchform = SearchForm()
    context = {
        "categories": categories,
        "srchform": srchform,
    }

    return render(request, "blog/about.html", context)

def contact(request):
    categories = Category.objects.all()
    srchform = SearchForm()

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
        "srchform": srchform,
        "form": ContactForm(),
    }

    return render(request, "blog/contact.html", context)

def search(request):
    sform = SearchForm(request.GET)
    results = []
    query = ''
    count = 0
    cmtcount = 0

    if sform.is_valid():
        query = sform.cleaned_data["post_title"]
        results = Post.objects.filter(post_title__icontains=query)
        count = results.count()
        # Fetch and annotate with comment count
        results = results.annotate(comment_count=Count('comments'))
        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(results, 2)  # Show 10 results per page
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        
    else:
        pass

    categories = Category.objects.all()
    srchform = SearchForm()

    # get only the first 3 posts randomly for the sidebar posts
    all_posts = list(Post.objects.all())
    random.shuffle(all_posts)
    random_posts = all_posts[:3]

    context = {
        "categories": categories,
        "random_posts": random_posts,
        "sform": sform,
        "results": results,
        'query': query,
        'count': count,
        'num_comments': cmtcount,
        'srchform' : srchform,
    }
    return render(request, "blog/search.html", context)

def shop(request):
    return HttpResponse("Shopping page")
