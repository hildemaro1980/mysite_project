from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post

admin.site.register(Post,TranslatableAdmin) # register for managing the app Post in Admin