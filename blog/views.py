from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import CommentForm


def landing_page(request):
    return render(request, 'landing_page.html')


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'author', 'content')



# Display a list of blog posts using a generic ListView
class PostList(generic.ListView):
    # Display a list of blog posts
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Handle GET requests for displaying a single blog post and its comments
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Display a single blog post and its comments
        queryset = Post.objects.filter(status=1)
        # Get the blog post with the specified slug
        post = get_object_or_404(queryset, slug=slug)
        # Annotate the post with the count of approved comments
        post_with_comment_count = Post.objects.annotate(
            comment_count=Count('comments')).get(slug=slug)

        # Get approved comments for the post and order by creation date
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        # Check if the current user has liked the post
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Render the post detail template with relevant data
        return render(
            request,
            "post_detail.html",
            {
                "post": post_with_comment_count,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    # Handle POST requests for adding new comments and toggling post likes
    @method_decorator(csrf_exempt)
    def post(self, request, slug, *args, **kwargs):
        # Handle posting a new comment on a blog post
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = post.likes.filter(id=request.user.id).exists()

        # Toggle the like status for the posts
        if liked:
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        comment_form = CommentForm(data=request.POST)

        # Handle the form data for adding a new comment
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            # Only initialize the form when it's not valid
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form  # Use the initialized form here
            },
        )


# Handle POST requests for toggling post likes
def like_post(request, post_id):
    # Toggle the like status for the post
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        likes_count = post.likes.count()

    # Return a JSON response indicating the success and current likes count
        return JsonResponse({"success": True, "likes_count": likes_count})
    else:
        # Return a JSON response indicating authentication failure
        return JsonResponse(
            {"success": False, "error": "User is not authenticated"}
            )


# Handle POST requests for toggling comment likes
def like_comment(request, comment_id):
    # Toggle the like status for the post
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.is_authenticated:
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            liked = False
        else:
            comment.likes.add(request.user)
            liked = True

        comment_likes_count = comment.likes.count()

        return JsonResponse(
            {"success": True, "comment_likes_count": comment_likes_count}
            )
    else:
        return JsonResponse(
            {"success": False, "error": "User is not authenticated"}
            )
