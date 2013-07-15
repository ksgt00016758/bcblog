from django import template
from django.utils.encoding import force_unicode

from creole import creole2html

from common import LOG
from blog.models import Tag

register = template.Library()


@register.filter(name='startswith')
def startswith(string, prefix):
    if isinstance(string, str) or isinstance(string, unicode):
        return string.startswith(prefix)
    LOG.error('[%s] is not str object, return False', string)
    return False


@register.filter(name='wiki2html')
def wiki2html(wiki_str):
    """
    To make this work, you need to copy creole package into your python path.
    """
    return creole2html(force_unicode(wiki_str))


MON_NAME = {1: 'JAN',
            2: 'FEB',
            3: 'MAR',
            4: 'APR',
            5: 'MAY',
            6: 'JUNE',
            7: 'JULY',
            8: 'AUG',
            9: 'SEPT',
            10: 'OCT',
            11: 'NOV',
            12: 'DEC',}
@register.filter(name='month_name')
def month_name(dt):
    """
    This may be replaced by default [date] filter: blog.created|date:'N'
    """
    LOG.debug('##### month is: %s', dt.month)
    return MON_NAME.get(dt.month)


class GetArticleTagsNode(template.Node):
    def __init__(self, variable):
        self.variable = variable

    def render(self, context):
        context[self.variable] = Tag.objects.all()
        return ''

@register.tag('get_article_tags')
def get_article_tags(parser, token):
    """
    Stores the name of the tags in the context.
    Usage::
        {% get_article_tag as tag_list %}
    """
    args = token.contents.split()
    if len(args) != 3 or args[1] != 'as':
        raise template.TemplateSyntaxError("'get_article_tags' requires "
                                  "'as variable' (got %r)" % args)
    return GetArticleTagsNode(args[2])