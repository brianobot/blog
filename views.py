from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import CommentForm
import random

class PostList(generic.ListView):
    queryset = Post.objects.filter(status="P").order_by('-created')
    template_name = 'blog/post_list.html'
    paginate_by = 7

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    # ranx = random.randint(post.pk - 1, post.pk + 1)
    next_post = post #Post.objects.exclude(slug=slug)[ranx]
    prev_post = post #Post.objects.exclude(slug=slug)[ranx - 1]
    comments = post.comments.all().order_by('created')
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the comment to the current post
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('blog:post_detail', post.slug)
    else: 
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'next_post': next_post,
                                           'prev_post': prev_post,
                                           })