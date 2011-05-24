from django.db import models
from bumblebee import settings 

class ImageUpload(models.Model):
    file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH)


class ImageDetail(models.Model):
    file = models.ForeignKey('ImageUpload')
    puzzle = models.ForeignKey('Puzzle')
    aviary_url = models.URLField(db_index=True)
    

class Source(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    
    def __unicode__(self):
        return self.name


class Grid(models.Model):
    rows = models.SmallIntegerField(db_index=True)
    columns = models.SmallIntegerField(db_index=True)

    def __unicode__(self):
        return '%(rows)s x %(columns)s' % {"rows":str(self.rows), "columns":str(self.columns)}


class Filter(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    source = models.ForeignKey('Source', db_index=True)
    
    def __unicode__(self):
        return self.name


class Difficulty(models.Model):
    value = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    grid = models.ForeignKey('Grid', db_index=True)
    filters = models.ManyToManyField('Filter', db_index=True)

    def __unicode__(self):
        return self.name
    
    
class Puzzle(models.Model):
    guid = models.CharField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    difficulty = models.ForeignKey('Difficulty')
    width = models.IntegerField(db_index=True)
    height = models.IntegerField(db_index=True)
    image = models.ManyToManyField('ImageUpload', through='ImageDetail', null=True, blank=True)
    
    def __unicode__(self):
        return self.name