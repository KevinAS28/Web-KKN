from django.contrib import admin
from polls_cms_integration import models as PollModel
# Register your models here.
class HomeCardImageAdmin(admin.ModelAdmin):    
    readonly_fields = ('tanggal',)
    extra = 3

# class HomeCardImageAdmin(admin.ModelAdmin):
#     model = PollModel.HomeCardImagePlugin
#     readonly_fields = ('votes',)
#     extra = 3


# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {
#             'fields': ['question'],
#         }),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question',)
#     search_fields = ['question']

# admin.site.register(Poll, PollAdmin)
admin.site.register(PollModel.HomeCardImagePlugin, HomeCardImageAdmin)
