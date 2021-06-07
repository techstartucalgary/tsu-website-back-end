"""TechStartBackEnd URL Configurations

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BackEnd import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('event-section', views.getEventSection.as_view(), name='Event Sections'),
    path('event-section/create', views.saveEventSection.as_view(), name='Save Event Section'),
    path('event-section/<int:pk>', views.updateEventSection.as_view(), name='Update Event Section'),
    path('event-section/<int:pk>/delete', views.deleteEventSection.as_view(), name='Delete Event Section'),
    path('event', views.getEvent.as_view(), name='Event'),
    path('event/create', views.saveEvent.as_view(), name='Save Event'),
    path('event/<int:pk>', views.updateEvent.as_view(), name='Update Event'),
    path('event/<int:pk>/delete', views.deleteEvent.as_view(), name='Delete Event'),
    path('post', views.getPost.as_view(), name='Posts'),
    path('create-post', views.createUserPost.as_view(), name='Create User Post'),
    path('update-post/<int:pk>', views.updateUserPost.as_view(), name='Update User Post'),
    path('delete-post/<int:pk>/delete', views.deleteUserPost.as_view(), name='Delete User Post'),
    path('comment', views.getComment.as_view(), name='Comments'),
    path('comment/create', views.saveComment.as_view(), name='Save Comment'),
    path('comment/<int:pk>', views.updateComment.as_view(), name='Update Comment'),
    path('comment/<int:pk>/delete', views.deleteComment.as_view(), name='Delete Comment'),
    path('login', views.customObtainAuthToken.as_view(), name='API Token Login'),
    path('register', views.RegisterUserView.as_view(), name='Register user'),
    path('ping', views.pingAppView, name='Ping Heroku Server'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
