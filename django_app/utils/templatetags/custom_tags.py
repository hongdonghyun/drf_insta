from django import template

register = template.Library()


#실제 템플릿에서 사용할 수 있도록 template.Library의 filter데코레이터 적용
@register.filter()
def query_string(q):
    # value에는 querydict가 온다
    # {% for k,v_list in request.GET.lists %}{% for v in v_list %}<span>&{{ k }}={{ v }}</span>{% endfor %}{% endfor %}
    ret = '?'
    # for k, v_list in q.lists():
    #     for v in v_list:
    #         ret += '&{}={}'.format(k, v)
    # return ret

    return '?' + '&'.join(['{}={}'.format(k, v) for k, v_list in q.lists() for v in v_list])

