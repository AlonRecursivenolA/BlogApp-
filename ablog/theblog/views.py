from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm


# those are the functions that are being sent as a response when the browser asks for a request from the urls.py
# def home(request):  # this is the part of views that gets a request from the url's and send it to the browser
#     return render(request, 'home.html', {})


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    #fields = '__all__' #['body']
    template_name = 'add_a_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        
        return reverse_lazy('ListView')
def LikeView(request, pk):
    liked = False
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        liked = False
        post.likes.remove(request.user)
    else:
        liked = True
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details',args=[str(pk)]))

class HomeListView(ListView):
    model = Post
    template_name = 'ListView.html'
    ordering = ['-post_date']


class HomeDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'

    def get_context_data(self, **kwargs):

        context = super(HomeDetailView,self).get_context_data()
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        context["total_likes"] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('author',)


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('author',)


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category__posts': category_posts})


class UpdateTheView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'edit_post.html'
    # fields = '__all__'


class DeleteTheView(DeleteView):
    model = Post
    template_name = 'delete_view.html'

    def get_success_url(self):
        return reverse_lazy('ListView')

# def home(request):
#     return render(request,'home.html',{})
#
