from django.contrib import admin

from .models import Post
# Register your models here.

#debemos registra simpre el modelo que se creo para que muestre en nuestra pagina
#de administracion
admin.site.register(Post)