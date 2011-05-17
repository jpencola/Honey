from django.contrib import admin
from bumblebee.puzzle.models import Difficulty, Filter, Grid, Puzzle, Source 

class SourceAdmin(admin.ModelAdmin): 
    fields = ('name',)

admin.site.register(Source, SourceAdmin)

 
class FilterAdmin(admin.ModelAdmin): 
    fields = ('name', 'source')

admin.site.register(Filter, FilterAdmin)
    
       
class GridAdmin(admin.ModelAdmin):
    fields = ('rows', 'columns')
    
admin.site.register(Grid, GridAdmin)


class DifficultyAdmin(admin.ModelAdmin):
    fields = ('name', 'grid', 'filters')
    
admin.site.register(Difficulty, DifficultyAdmin)


class PuzzleAdmin(admin.ModelAdmin):
    fields = ('guid', 'name', 'difficulty')
    
admin.site.register(Puzzle, PuzzleAdmin)