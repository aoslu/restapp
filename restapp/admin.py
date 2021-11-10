from django.contrib import admin
from restapp.models import Gazeteci, Makale, Customers, KategoriModel
# Register your models here.
admin.site.register(Makale)

class GazeteciAdmin(admin.ModelAdmin):
    list_display= ('isim','soyisim','biyografi',)
admin.site.register(Gazeteci,GazeteciAdmin)

admin.site.register(KategoriModel)

class CustomersAdmin(admin.ModelAdmin):
    list_display= ('name', 'surname', 'comment', 'puan')
    search_fields = ('name',)
admin.site.register(Customers, CustomersAdmin)