from django.http import HttpResponse
from blog.serializers import ArticleSerializer,CommentSerializer,LabelSerializer
from blog.models import Article,Comments,Label
from blog.models import AdminIMG #富文本编辑器的图片模型
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView



class Labelview(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                GenericAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)





class ArticleView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)





class CommentsView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    def get(self,request,*args,**kwargs):
        self.request
        return self.list(request,*args,**kwargs)

def uploadIMG(self,request):
    self.request
    img = request.FILES.get('img')
    adminIMG = AdminIMG()
    adminIMG.filename = img.name
    adminIMG.img = img
    adminIMG.save()
    return HttpResponse(
                "<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s')."
                "closest('.mce-window').find('.mce-primary').click();</script>" % adminIMG.img)