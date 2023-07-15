from django.urls import path
from stores.views import StoreListCreateView, ProductListCreateView, StoreDetailsAPIView, AvailableProductListView

urlpatterns = [
    path('', StoreListCreateView.as_view(), name='store-list-create-view'),
    path('<int:store_id>/products/', ProductListCreateView.as_view(), name='product-list-create-view'),
    path('<str:store_link>/details/', StoreDetailsAPIView.as_view(), name='store-detail-view'),
    path('<str:store_link>/available-products/', AvailableProductListView.as_view(), name='available-product-list-view'),
]