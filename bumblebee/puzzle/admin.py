from django.contrib import admin
from bumblebee.puzzle.models import Difficulty, Filter, Grid, Puzzle, Source, ImageUpload, ImageDetail

class ImageDetailInline(admin.TabularInline):
    model = ImageDetail
    max_num = 1
    extra = 1


class ImageUploadAdmin(admin.ModelAdmin):
    inlines = (ImageDetailInline,)

admin.site.register(ImageUpload, ImageUploadAdmin)


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
    fields = ('name', 'grid', 'filters', 'value')
    
admin.site.register(Difficulty, DifficultyAdmin)


class PuzzleAdmin(admin.ModelAdmin):
    inlines = (ImageDetailInline,)
    fields = ('guid', 
              'name', 
              'difficulty',
              )
    
admin.site.register(Puzzle, PuzzleAdmin)