from django import shortcuts
from django.template import RequestContext
from django.core.urlresolvers import reverse

from blog.models import Article, Tag

def home(request):
    blogs = Article.objects.filter(is_valid=True)
        
    return shortcuts.render_to_response('list.html', {'blogs': blogs})
    
    
def detail(request, post_id):
    blog = shortcuts.get_object_or_404(Article, id=post_id)
    return shortcuts.render_to_response('detail.html',
                {'blog': blog, 'next': reverse('post-detail', args=[post_id])},
                context_instance=RequestContext(request))


def list_by_tag(request, tag_id):
    tag = shortcuts.get_object_or_404(Tag, id=tag_id)
    blogs = tag.article_set.filter(is_valid=True)
    return shortcuts.render_to_response('list.html', {'blogs': blogs, 'tag': tag})


def search(request):
    keyword = request.REQUEST.get('keyword')
    
    blogs = Article.objects.filter(is_valid=True)
    if keyword:
        blogs = blogs.filter(title__contains=keyword)
    
    return shortcuts.render_to_response('list.html', {'blogs': blogs, 'keyword': keyword})
