from django.urls import path
from .views import ProductCreateView,FetchProducts

urlpatterns = [
    path('/createproduct', ProductCreateView.as_view(),name="creteproduct"),
    path('/fetchprducts',FetchProducts.as_view())
]