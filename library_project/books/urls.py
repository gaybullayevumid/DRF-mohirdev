from django.urls import path
from .views import BookListApiView

urlpatterns = [
    path('', BookListApiView.as_view(),)
]
