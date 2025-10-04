from django.contrib import admin
from .models import Countries, Departaments,Cities,User
# Register your models here.
admin.site.register(Countries),

admin.site.register(Departaments),

admin.site.register(Cities),

admin.site.register(User)

class CountriesAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev', 'get_status')

    def get_status(self, obj):
        return "Activate" if obj.status else "Inactive"
    get_status.short_description = 'Status' #Table label    