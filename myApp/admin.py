from django.contrib import admin
from .models import Login, Signup, QNA, Index_gmails, Owner, ContactForm, RecycleForm
# Register your models here.
admin.site.register(Login)
admin.site.register(Signup)
admin.site.register(QNA)
admin.site.register(Index_gmails)
admin.site.register(Owner)
admin.site.register(ContactForm)
admin.site.register(RecycleForm)