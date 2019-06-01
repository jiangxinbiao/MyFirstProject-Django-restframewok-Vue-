
import xadmin
# Register your models here.
from .models import Article,Label,Comments,AdminIMG


class ArticleAdmin(object):
    list_display = ['photo','title','text','Cname','updatedtime']
    search_fields = ['photo','title','text','Cname','updatedtime']
    list_filter = ['photo','title','text','Cname','updatedtime']
    style_fields = {'text': 'ueditor'}
    list_per_page = 10
    list_eitable = ['text']
    model_icon = 'fa fa-list'

class LabelAdmin(object):
    list_display = [ 'name', ]
    search_fields = [ 'name',  'updatetime']
    list_filter = [ 'name', 'updatetime']
    model_icon = 'fa fa-list'
class CommentsAdmin(object):
    list_display = ['name', 'email', 'body', 'created','post']
    search_fields = ['name', 'email', 'body', 'created','post']
    list_filter = ['name', 'email', 'body', 'created','post']
    model_icon = 'fa fa-cog fa-spin'
class AdminIMGAdmin(object):
    list_display = ['filename', 'img']
    search_fields = ['filename', 'img']

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Label,LabelAdmin)
xadmin.site.register(Comments,CommentsAdmin)
xadmin.site.register(AdminIMG,AdminIMGAdmin)