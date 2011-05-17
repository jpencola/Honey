from django.db import models

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
    name = models.CharField(max_length=32, db_index=True)
    grid = models.ForeignKey('Grid', db_index=True)
    filters = models.ManyToManyField('Filter', db_index=True)

    def __unicode__(self):
        return self.name
    
    
class Puzzle(models.Model):
    guid = models.CharField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    difficulty = models.ForeignKey('Difficulty')
    #image = models.ImageField()
    
    def __unicode__(self):
        return self.name