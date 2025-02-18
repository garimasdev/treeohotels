from django.contrib import admin

from users.models import *

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(AgentProfile)
admin.site.register(VendorProfile)
admin.site.register(CustomerProfile)
