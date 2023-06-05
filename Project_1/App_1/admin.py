from django.contrib import admin
from App_1.models import Contact,Book,User,Order,Return1

admin.site.register(Contact), #Registers your model here.After doing this goto the apps.py file and copy the name of your app and paste it into settings.py in installed apps section with App_1.apps.Copied_name.
admin.site.register(Book),
admin.site.register(User),
admin.site.register(Order),
admin.site.register(Return1),
# Register your models here.
