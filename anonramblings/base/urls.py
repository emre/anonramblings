from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings


from ramblings.views import index, post, about, thanks, detail


urlpatterns = [
    path('%s/' % settings.CUSTOM_ADMIN_PATH, admin.site.urls),
    path('', index, name="index"),
    path('trending', index, name="trending"),
    path('post', post, name="post"),
    path('post/<slug:permlink>', detail, name="post_detail"),
    path('thanks/', thanks, name="thanks"),
    path('about', about, name="about"),
    url(r'^markdownx/', include('markdownx.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)