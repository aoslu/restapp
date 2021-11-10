from django.urls import path
from restapp.api import views as api_views

urlpatterns = [
  #  path('urunlerim/', api_views.urun_list_create_api_view, name= 'urun-listesi')
    path('customers/', api_views.CustomerListCreateAPIView.as_view(), name= 'musteri-listesi'),
    path('customers/<int:pk>', api_views.CustomerDetailAPIView.as_view(), name= 'musteri-listesi-detay'),
    path('products/', api_views.ProductModelListCreateAPIView.as_view(), name= 'urun-listesi'),
    path('products/<int:pk>', api_views.ProductModelDetailAPIView.as_view(), name= 'urun-listesi-detay'),
    path('kategori/', api_views.KategoriModelListCreateAPIView.as_view(), name= 'kategori-listesi'),
    path('kategori/<int:pk>', api_views.KategoriModelDetailAPIView.as_view(), name= 'kategori-listesi-detay'),
    path('makale/', api_views.MakaleListCreateAPIView.as_view(), name= 'makale-listesi'),
    path('makale/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name= 'makale-listesi-detay'),
    path('gazeteci/', api_views.GazeteciListCreateAPIView.as_view(), name= 'gazeteci-listesi'),
    path('gazeteci/<int:pk>', api_views.GazeteciDetailAPIView.as_view(), name= 'gazeteci-listesi-detay'),
#    path('user/', api_views.CustomUserModelListCreateAPIView.as_view(), name= 'user-listesi'),
#    path('user/<int:pk>', api_views.CustomUserModelDetailAPIView.as_view(), name= 'user-listesi-detay'),
]


# FUNCTİON BASED VİEWS
# urlpatterns = [
#   #  path('urunlerim/', api_views.urun_list_create_api_view, name= 'urun-listesi')
#     path('customers/', api_views.customer_list_create_api_view, name= 'musteri-listesi'),
#     path('customers/<int:pk>', api_views.customer_detail_api_view, name= 'musteri-listesi-detay'),
# ]