from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)