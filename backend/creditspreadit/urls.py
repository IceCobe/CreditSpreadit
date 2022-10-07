from django.urls import path, include
from rest_framework import routers                 
from creditspreadit import views                             

router = routers.DefaultRouter()                   
router.register('daterange', views.DateRangeView)  
router.register('category', views.CategoryView)  
router.register('bonus', views.BonusView)  
router.register('creditcard', views.CreditCardView)  

urlpatterns = [
    path('api/', include(router.urls))        
]
