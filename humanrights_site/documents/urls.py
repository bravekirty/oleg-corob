from django.urls import path
from documents import views


app_name = 'documents'
urlpatterns = [
    path('', views.AllAttachmentsListView.as_view(), name='all-attachments'),
    path('attachment/<int:pk>/', views.AttachmentDetailView.as_view(), name='attachment_detail'),
    path('attachment/<int:pk>/view/', views.attachment_file_view, name='attachment_view'),
]
