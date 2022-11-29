from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog.views import blog, post, category_post_list, allposts


urlpatterns = [
    path('', blog, name = 'blog'),
    path('post/<slug>/', post, name = 'post'),
    path('postlist/<slug>/', category_post_list, name = 'postlist'),
    path('posts/', allposts, name = 'allposts'),
]