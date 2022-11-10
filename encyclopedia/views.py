from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
import markdown2


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),

    })

def page(request, title):
    entryText = util.get_entry(title)
    for page in util.list_entries():
        if page == title:
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "entry": markdown2.markdown(entryText)
            })
    return HttpResponseNotFound('<h1> Entry not found </h1>')


