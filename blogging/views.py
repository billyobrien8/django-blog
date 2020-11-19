from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)
    template_name = 'blogging/list.html'


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'
