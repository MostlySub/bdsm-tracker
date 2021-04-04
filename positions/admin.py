from django.contrib import admin

from .models import Position, PositionRequiredWhen, PositionImage

admin.site.register(Position)
admin.site.register(PositionRequiredWhen)
admin.site.register(PositionImage)
