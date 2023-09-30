from django.contrib import admin
from commandapp.models import Details

class DetailsAdmin(admin.ModelAdmin):

    list=['title','commands','date']


admin.site.register(Details,DetailsAdmin)

