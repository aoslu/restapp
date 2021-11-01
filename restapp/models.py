from django.db import models
from django.db.models.fields import TextField

class Gazeteci(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    biyografi = models.CharField(max_length=50)

    def _str__(self):
        return f'{self.isim} {self.soyisim}'
# Create your models here.
class Makale(models.Model):
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name=)
    baslik = models.CharField(max_length=50)
    metin = models.TextField()
    sehir = models.CharField(max_length=50)
    yaratilma_tarihi= models.DateTimeField(auto_now_add=True)
    aktif = models.BooleanField()
    guncellenme_tarihi = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.baslik

class Customers(models.Model):
    name= models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    puan= models.IntegerField()
    comment= models.CharField(max_length=50)

    class Meta:
        db_table='customer'
        verbose_name='Customer'
        verbose_name_plural='Customers'

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    baslik= models.CharField(max_length= 50)
    fiyat_ekle=models.SmallIntegerField()
    aciklama= models.CharField(max_length=350)
    olusturulma_tarihi= models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table= 'urunler'
        verbose_name='Ürün'
        verbose_name_plural='Ürünler'

    def __str__(self):
        return self.baslik

class KategoriModel(models.Model):
    isim = models.CharField( max_length=40, blank=False,null=False)

    class Meta:
        db_table='kategori'
        verbose_name='Kategori'
        verbose_name_plural='Kategoriler'

    def __str__(self):
        return self.isim