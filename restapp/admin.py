from django.contrib import admin
from restapp.models import Makale, Customers, KategoriModel
# Register your models here.
admin.site.register(Makale)

admin.site.register(KategoriModel)
class CustomersAdmin(admin.ModelAdmin):
    list_display= ('name', 'surname', 'comment', 'puan')
    search_fields = ('name',)
admin.site.register(Customers, CustomersAdmin)