from django import db
from django import shortcuts

from api import forms
from api import models
from api import helpers


def get_link(request):
    if request.method == 'GET':
        form = forms.LinkForm()
    elif request.method == 'POST':
        form = forms.LinkForm(request.POST)
        if form.is_valid():
            host = helpers.get_host(request)
            original_link = form.cleaned_data['link']
            link = models.Link.create(host, original_link)
            try:
                link.save()
                status = 201
            except db.IntegrityError:
                link = models.Link.objects.get(original_link=original_link)
                status = 200
            return shortcuts.render(request, 'api/success.html',
                                    {'short_link': link.short_link},
                                    status=status)
    return shortcuts.render(request, 'api/main.html', {'form': form})


def redirect_link(request, link_id):
    if request.method == 'GET':
        host = helpers.get_host(request)
        short_link = models.Link.get_short_link(host, link_id)
        link = models.Link.objects.filter(short_link=short_link).first()
        if link:
            link.visited()
            return shortcuts.redirect(link.original_link)
    return shortcuts.redirect('/')
