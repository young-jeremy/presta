from django.shortcuts import render


def blogs_home(request):
    template_name = 'blog/small_business.html'
    return render(request, template_name)


def blog_post(request):
    template_name='blog/blog_post.html'
    return render(request, template_name)