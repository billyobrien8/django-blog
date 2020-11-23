from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.utils import timezone
from blogging.forms import MyPostForm


class BlogListView(ListView):
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


def add_model(request):

    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.published_date = timezone.now()
            model_instance.save()
            return redirect("/")

    else:

        form = MyPostForm()

        return render(request, "blogging/add.html", {"form": form})
