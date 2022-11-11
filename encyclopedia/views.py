from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
import markdown2


from . import util

def SearchSublist(text):
    entries = util.list_entries()
    newEntries = []
    for entry in entries:
        if text in entry:
            newEntries.append(entry)
    return newEntries


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


def pageSearch(request):
    entryText = util.get_entry(request.GET.get('q'))
    for page in util.list_entries():
        if page == request.GET.get('q'):
            return render(request, "encyclopedia/entry.html", {
                "title": request.GET.get('q'),
                "entry": markdown2.markdown(entryText)
            })
    return render(request,"encyclopedia/search.html", {
        "entries": SearchSublist(request.GET.get('q'))
    })

