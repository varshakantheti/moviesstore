from django.contrib import admin
from .models import Order, Item, Feedback

admin.site.register(Order)
admin.site.register(Item)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'date']
    list_filter = ['date']
    search_fields = ['name', 'feedback_text']
    readonly_fields = ['date']

admin.site.register(Feedback, FeedbackAdmin)
