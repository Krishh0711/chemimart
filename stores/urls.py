from django.urls import path
from stores.views import StoreListCreateView

urlpatterns = [
    path('', StoreListCreateView.as_view(), name='store-list-create-view'),
]