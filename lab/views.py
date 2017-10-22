from django.template.loader import get_template
from django.http import HttpResponse


from datetime import datetime
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)