from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import EducationBlogPost
from .forms import EducationBlogPostForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required


def education_post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'eductionblogposts.html' template
    """
    posts = EducationBlogPost.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "education_center/education_blogposts.html", {'posts': posts})


def education_post_detail(request, id):
    post = get_object_or_404(EducationBlogPost, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "education_center/education_postdetail.html", {'post': post})


def education_top_posts(request):
    posts = EducationBlogPost.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-views')[:5]
    return render(request, "education_center/education_blogposts.html", {'posts': posts})


@staff_member_required
def education_new_post(request):
    if request.method == "POST":
        form = EducationBlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(education_post_detail, post.pk)
    else:
        form = EducationBlogPostForm()
    return render(request, 'education_center/education_blogpostform.html', {'form': form})


@staff_member_required
def education_edit_post(request, id):
    post = get_object_or_404(EducationBlogPost, pk=id)
    if request.method == "POST":
        form = EducationBlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(education_post_detail, post.pk)
    else:
        form = EducationBlogPostForm(instance=post)
    return render(request, 'education_center/education_blogpostform.html', {'form': form})
