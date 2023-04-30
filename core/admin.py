from django.contrib import admin

# Register your models here.

from .models import (
    Contact, Fashion, Jewellery,Electronic,User,Login,Home

)


admin.site.register(Contact)
admin.site.register(Fashion)
admin.site.register(Jewellery)
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Home)
admin.site.register(Electronic)



