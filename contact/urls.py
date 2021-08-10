from django.urls import path
from .views import ContactView, MessageView

urlpatterns = [
    path('contct_form/', ContactView.as_view(), name='contact_form'),
    path('message/<str:visitor>/<int:result>', MessageView.as_view(), name='message'),
]
