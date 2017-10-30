# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from lab.models import Laboratory, Teacher, Student, Project, Research, Information, Activity, Resource, Prize, TeacherProject, TeacherResearch, StudentProject, StudentResearch,Image

# Register your models here.


class LaboratoryAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class ResearchAdmin(admin.ModelAdmin):
    pass


class InformationAdmin(admin.ModelAdmin):
    pass


class ActivityAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

class PrizeAdmin(admin.ModelAdmin):
    pass


class TeacherProjectAdmin(admin.ModelAdmin):
    pass


class TeacherResearchAdmin(admin.ModelAdmin):
    pass


class StudentProjectAdmin(admin.ModelAdmin):
    pass


class StudentResearchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Laboratory,LaboratoryAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Research,ResearchAdmin)
admin.site.register(Information,InformationAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Resource,ResearchAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(TeacherProject, TeacherProjectAdmin)
admin.site.register(TeacherResearch, TeacherResearchAdmin)
admin.site.register(StudentProject, StudentProjectAdmin)
admin.site.register(StudentResearch, StudentResearchAdmin)







