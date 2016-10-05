from django.contrib import admin
from my_app.models import Rater, Item, Data

admin.site.register([Rater, Item, Data])
