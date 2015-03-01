# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context,RequestContext

from projects.models import Entry,Project
import datetime,pytz

datetime.datetime.now(pytz.utc)

def log(request,page=1):
    c = RequestContext(request)
    
    now = datetime.datetime.now(pytz.utc)
    e = Entry.objects.filter(posted__lte=now)
    c['entries'] = e
    
    return render_to_response('log.html', c)

def log_2014(request,page=1):
    c = RequestContext(request)
    
    now = datetime.datetime.now(pytz.utc)
    e = Entry.objects.filter(posted__lte=now)
    c['entries'] = e
    
    return render_to_response('log_2014.html', c)

def log_perma(request,project,slug,v2014=False):
    c = RequestContext(request)
    
    e = get_object_or_404(Entry,slug=slug)
    c['e'] = e
    
    if v2014:
        return render_to_response('log_perma_2014_2.html', c)
    return render_to_response('log_perma.html', c)

def log_project(request,slug,v2014=False):
    c = RequestContext(request)
    
    p = get_object_or_404(Project,slug=slug)
    now = datetime.datetime.now(pytz.utc)
    c['entries'] = p.projectentry.filter(posted__lte=now)
    c['project'] = p
    if v2014:
        return render_to_response('log_project_2014.html', c)
    else:
        return render_to_response('log_project.html', c)

def project_list(request):
    c = RequestContext(request)
    p = Project.objects.all()
    c['projects'] = p
    
    return render_to_response('projects.html', c)

def project_list_2014(request):
    c = RequestContext(request)
    p = Project.objects.all()
    c['projects'] = p
    
    return render_to_response('projects_2014_2.html', c)