from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Kogo E-Commerce Admin"
admin.site.site_title="Kogo E-Commerce Admin"
admin.site.index_title="Kogo E-Commerce Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
    path('', include('ecommerce.urls',namespace='ecom')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)