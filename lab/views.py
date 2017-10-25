from django.template.loader import get_template
from django.http import HttpResponse


from datetime import datetime
# Create your views here.
def test(request):
    """
    测试页
    :param request:
    :return:
    """
    template = get_template('test.html')
    html = template.render()
    return HttpResponse(html)

def homepage(request):
    """
    主页，导航页
    :param request:
    :return:
    """
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)

def brief_introduction_of_laboratory(request):
    """
    实验室简介页
    :param request:
    :return:
    """
    template = get_template('brief_introduction_of_laboratory/brief_introduction_of_laboratory.html')
    html = template.render()
    return HttpResponse(html)