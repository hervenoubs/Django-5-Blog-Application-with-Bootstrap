from django import forms
from .models import Category
from blog.models import Post

class WritePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_title', 'post_intro', 'post_content', 'post_banner']

    post_title = forms.CharField(
        required = True,
        max_length = 255,
        widget = forms.TextInput(
            attrs={"class": "form-control mb-3"}
        ),
    )
    post_intro = forms.CharField(
        required = True,
        max_length= 255,
        widget = forms.TextInput(
            attrs={"class": "form-control mb-3"}
        ),
    )
    # post_slug = forms.CharField(
    #     required = True,
    #     max_length=255,
    #     widget = forms.TextInput(
    #         attrs={"class": "form-control"}
    #     ),
    # )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check form-check-inline"}),
    )
    post_content = forms.CharField(
        required=True,
        widget = forms.Textarea(
            attrs={"class": "form-control mb-3"}
        ),
    )
    post_banner = forms.ImageField(
        required=True,
        widget= forms.FileInput(
            attrs={"class": "form-control mb-3"}
        ),
    )

class CommentForm(forms.Form):
    visitor_name = forms.CharField(
        required=True,
        max_length = 60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
        label = "Your name",
    )
    visitor_email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter a valid Email address"}
        ),
        label = "Your Email",
    )

    visitor_comment = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter your comment here"}
        ),
        label = "Your comment",
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length = 60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
        label = "Your name",
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter a valid Email address"}
        ),
        label = "Your Email",
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter your comment here"}
        ),
        label = "Your comment",
    )

class NewsletterForm(forms.Form):
    firstname = forms.CharField(
        required = True,
        max_length=155,
        widget = forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Firstname"}
        ),
        label="Firstname",
    )

    email = forms.EmailField(
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email address"}
        ),
        label = "Email address",
    )

class SearchForm(forms.Form):
    post_title = forms.CharField(
        required=True,
        widget= forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Find an article"}
        ),
    )