from django.contrib import admin
from .models import Project, Projectlink, Testing
# Register your models here.

class ProjectlinkAdmin(admin.ModelAdmin):
    pass

class ProjectlinkInline(admin.TabularInline):
    model = Projectlink

#class TestingAdmin(admin.ModelAdmin):
  #  pass
#class TestingInline(admin.TabularInline):
  #  model = Testing

class ProjectAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ("projectnumber", "title")
    list_filter = ("status", )
    search_fields = ("projectnumber__startswith", "title__startswith")
    inlines = [ProjectlinkInline]
    pass





admin.site.register(Project, ProjectAdmin)
admin.site.register(Projectlink, ProjectlinkAdmin)
#admin.site.register(Testing, TestingAdmin)
