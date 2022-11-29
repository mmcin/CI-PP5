from django.conf import settings
from django.contrib import admin
from blog.views import blog
from django.urls import path
# post, about, search, postlist, allposts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog, name = 'blog'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('postlist/<slug>/', postlist, name = 'postlist'),
    path('posts/', allposts, name = 'allposts'),
]