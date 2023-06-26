from django.contrib import admin
from .models import Person, Institution, Subject, Role, Cargo, PersonSubject

# Register your models here.
class RoleInLine(admin.TabularInline):
    model = Role
    extra = 1

class PersonSubjectInLine(admin.TabularInline):
    model = PersonSubject
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    #filter_horizontal = ('institutions','subjects')
    inlines = (RoleInLine, PersonSubjectInLine)

class PersonInLine(admin.TabularInline):
    model = Person

class InstitutionAdmin(admin.ModelAdmin):
    inlines = (RoleInLine,)
    #fields = ('name', 'people')

class SubjectAdmin(admin.ModelAdmin):
    inlines = (PersonSubjectInLine,)
    #fields = ('subject', 'people')

admin.site.register(Person, PersonAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Cargo)
