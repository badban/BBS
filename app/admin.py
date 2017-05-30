from django.contrib import admin
from app.models import BBS, BBS_user, Category, Comment

class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'view_count', 'created_date')
    list_filter=('created_date',)
    search_fields =('title', 'author__user__username')

    def signature(self, obj):
        return obj.author.signature
    signature.short_description  = 'hah'

# class BBS_user_admin(admin.ModelAdmin):
#    list_display = ('username', 'email', 'signature', )


admin.site.register(BBS, BBS_admin)
admin.site.register(BBS_user)
admin.site.register(Category)
admin.site.register(Comment)

