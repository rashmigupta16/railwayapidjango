from django.contrib import admin

# Register your models here.

from .models import User, ChatHistory


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email_id', 'created_at', 'updated_at',)
    # list_per_page = 10
    search_fields = ('user_id','first_name')
    save_as = True
    actions_on_top = False


admin.site.register(User, UserAdmin)
admin.site.register(ChatHistory)
