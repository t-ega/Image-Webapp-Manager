from django.urls import path
from .views import upload_images, AdminPanel, imageEdit

urlpatterns = [
    path('', AdminPanel.as_view(), name='admin-panel'),
    path('edit-image/<str:public_id>', imageEdit, name='edit-image'),
    path('upload', upload_images, name='upload-image'),

]
