from django.urls import path
from profiles import views

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view())
]
