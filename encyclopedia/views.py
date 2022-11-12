from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
import markdown2


from . import util

def SearchSublist(text):
    entries = util.list_entries()
    newEntries = []
    for entry in entries:
        if text in entry or text.capitalize() in entry or text.upper() in entry:
            newEntries.append(entry)
    if not len(newEntries) == 0:
        return newEntries
    else:
        return None


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
    q =  request.GET.get('q')
    for page in util.list_entries():
        if page == q:
            return render(request, "encyclopedia/entry.html", {
                "title": q,
                "entry": markdown2.markdown(util.get_entry(q))
            })
        elif page == q.upper():
            return render(request, "encyclopedia/entry.html", {
            "title": q.upper(),
            "entry": markdown2.markdown(util.get_entry(q.upper()))
            })
        elif page == q.capitalize():
            return render(request, "encyclopedia/entry.html", {
            "title": q.capitalize(),
            "entry": markdown2.markdown(util.get_entry(q.capitalize()))
            })

    return render(request,"encyclopedia/search.html", {
        "entries": SearchSublist(request.GET.get('q'))
    })

def pageNew(request):
    return render(request,"encyclopedia/new.html")

def entrySave(request):
    entryText = request.GET.get('newEntry')
    if entryText.split()[0] == "#":
        entryName = entryText.split()[1]
    elif entryText.split()[0][0] == "#":
        entryName = entryText.split()[0][1:]
    else:
        entryName = entryText.split()[0]
    util.save_entry(entryName, entryText)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),

    })

