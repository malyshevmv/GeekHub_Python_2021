from django.contrib import admin
from django.urls import path, re_path, include
from product_catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'^products/$', views.ProductListView.as_view(), name='products'),
    re_path(r'^products/product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view()),
    re_path(r'^category/(?P<pk>\d+)$', views.cat, name='category_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
