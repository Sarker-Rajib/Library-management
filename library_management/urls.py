from django.contrib import admin
from django.urls import path, include
from .views import homepage

# ------------------------------
from django.conf import settings
from django.conf.urls.static import static
#------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('books/<slug:category_slug>/',homepage, name='filterView'),
    path('user/', include('User.urls')),
    path('book/', include('Books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)