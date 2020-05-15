from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from ramblings.views import index, post, about, thanks, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('post', post, name="post"),
    path('post/<slug:permlink>', detail, name="post_detail"),
    path('thanks/', thanks, name="thanks"),
    path('about', about, name="about"),
    url(r'^markdownx/', include('markdownx.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)