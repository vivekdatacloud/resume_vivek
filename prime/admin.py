from django.contrib import admin
from .models import *
# Register your models here.

class contact_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')


admin.site.register(hero_section)
admin.site.register(skill_section)
admin.site.register(course_list)
admin.site.register(project_list)
admin.site.register(acadamics_details)
admin.site.register(get_touch)
admin.site.register(footer)
admin.site.register(contact_us,contact_usAdmin)
admin.site.register(skill_icon)
