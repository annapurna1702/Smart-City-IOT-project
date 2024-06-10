from django.urls import path
from . import views



app_name='credentials'

urlpatterns = [
    
    path('',views.index,name='index'),
    path('signIn',views.signIn,name='signIn'),
    path('logout',views.logout,name='logout'),
    path('mypage',views.myfunction),
    path('method',views.method),
    path('demo',views.demo),

    #ADMIN
    path('Admin',views.admin_index,name='AdminHome'),
    path('addMuninicipality',views.addMuninicipality,name='addMuninicipality'),

    #Municipality
    path('municipality',views.municipalityHome,name='municipalityHome'),
    path('AddWasteBin',views.AddWasteBin,name='AddWasteBin'),
    path('AddCollectionAgent',views.AddCollectionAgent,name='AddCollectionAgent'),

    #Collection Agent
    path('Home',views.collectionAgent_home,name='collectionAgent_home'),


]