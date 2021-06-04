from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'members'

urlpatterns = [
	path('register/',views.UserRegisterView.as_view(),name='register'),
	path('login/',views.UserLoginView.as_view(),name='login'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)