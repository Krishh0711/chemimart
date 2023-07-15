from django.urls import path
from stores.views import StoreListCreateView, ProductListCreateView

urlpatterns = [
    path('', StoreListCreateView.as_view(), name='store-list-create-view'),
    path('<int:store_id>/products/', ProductListCreateView.as_view(), name='product-list-create-view'),
]