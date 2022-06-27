from django.contrib import admin
from .models import Contact, Movie

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'subject', 'message']
    list_display = ['name', 'email', 'subject', 'message']
    search_fields = ['name', 'email', 'subject', 'message']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


class MovieAdmin(admin.ModelAdmin):
    fields = ['name', 'director', 'cast', 'generes', 'release_year', 'country', 'description', 'url', 'thumbnail']
    list_display = ['name', 'director', 'cast', 'generes', 'release_year', 'country', 'description', 'url', 'thumbnail']
    search_fields = ['name', 'director', 'cast', 'generes', 'release_year', 'country', 'description']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Contact, ContactAdmin)
admin.site.register(Movie, MovieAdmin)
