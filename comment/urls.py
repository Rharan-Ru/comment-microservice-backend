from django.urls import path

from .views import CommentsView

urlpatterns = [
    path('comment', CommentsView.as_view(), name='comment_view')
]
