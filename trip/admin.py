from django.contrib import admin
from trip.models import Place, Restaurant, Activity, Bar

# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Activity)
admin.site.register(Bar)
