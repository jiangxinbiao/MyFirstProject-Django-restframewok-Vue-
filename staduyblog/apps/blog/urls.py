from django.conf.urls import url

from blog.views import ArticleView, CommentsView, Labelview

urlpatterns = [
    url(r'^Article/', ArticleView.as_view(), name='Article'),
    url(r'^Comments/', CommentsView.as_view(), name='Comments'),
    url(r'^Label/', Labelview.as_view(), name='Label'),
]