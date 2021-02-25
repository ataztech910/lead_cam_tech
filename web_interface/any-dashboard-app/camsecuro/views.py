from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required
def index(request, id):
    template = loader.get_template('camsecuro/index.html')
    context = { 'id': id }
    return HttpResponse(template.render(context, request))


@login_required
def place(request):
    template = loader.get_template('camsecuro/place.html')
    context = {}
    return HttpResponse(template.render(context, request))



