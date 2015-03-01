from django.db import models
from uuidfield import UUIDField

import datetime,pytz

# Create your models here.

class Project(models.Model):
    
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    blurb = models.TextField(null=True,blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    display_class = models.CharField(max_length=32, default="bh_dots")
    
    def __unicode__(self):
        return self.name

    @property
    def entries(self):
        return self.projectentry.filter(posted__lte=datetime.datetime.now(pytz.utc))
    
    @property
    def latest_entry(self):
        return self.entries.latest()
    
    @property
    def first_entry(self):
        return self.entries.reverse()[0]
    
    @property
    def entry_count(self):
        return self.entries.count()
    

class ExternalProjectLink(models.Model):
    """
    A link to something else
    """
    project = models.ForeignKey('Project', related_name="links")
    url = models.URLField(max_length=256)
    icon = models.CharField(max_length=32, null=True, blank=True, default="fa-external-link")
    
        
class Entry(models.Model):

    project = models.ForeignKey('Project',related_name="projectentry")
    title = models.CharField(max_length=32)
    slug = models.SlugField()
    body = models.TextField()
    
    posted = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-posted']
        get_latest_by = "posted"
        
    def __unicode__(self):
        return self.title
    
    @property
    def is_viewable(self):
        if datetime.datetime.now(pytz.utc) >= self.posted:
            return True
        else:
            return False
        
    @property
    def get_prev_in_proj(self):
        try:
            x = self.get_previous_by_posted(project=self.project)
            return x
        except:
            return False
    @property
    def get_next_in_proj(self):
        try:
            x = self.get_next_by_posted(posted__lte=datetime.datetime.now(pytz.utc))
            return x
        except:
            return False
    @property
    def get_prev(self):
        try:
            x = self.get_previous_by_posted(posted__lte=datetime.datetime.now(pytz.utc))
            return x
        except:
            return False
    
    @property
    def get_next(self):
        try:
            x = self.get_next_by_posted()
            return x
        except:
            return False

class InlineEntryImg(models.Model):
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    
    title           = models.CharField(max_length=128)
    
    image           = models.ImageField(upload_to='projects')
    identifier      = UUIDField(auto=True,max_length=8)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-title']