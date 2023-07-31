from django.urls import path, include
from profil_desa_jarakan import views

urlpatterns = [    
    path('contact/', views.contact_view),
    path('generate-surat/', views.generate_surat, name='generate_surat_form'),

]