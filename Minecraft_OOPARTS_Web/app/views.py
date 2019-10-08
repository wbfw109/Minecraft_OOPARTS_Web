"""
Definition of views.
"""


from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime



def show(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/show.html',
        {
            'title':'',
            'message':'',
            'year':datetime.now().year,
        }
    )


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Main',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Please,',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'안녕하십니까?',
            'year':datetime.now().year,
        }
    )


def feature(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/feature.html',
        {
            'title':'Feature',
            'message':'차별화된 운영 !',
            'year':datetime.now().year,
        }
    )


def history(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/history.html',
        {
            'title':'History',
            'message':'역사 ...',
            'year':datetime.now().year,
        }
    )



def environment(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/environment.html',
        {
            'title':'Environment',
            'message':'환경 ...',
            'year':datetime.now().year,
        }
    )



def best(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/best.html',
        {
            'title':'Best',
            'message':'최고의 건축물 !',
            'year':datetime.now().year,
        }
    )

