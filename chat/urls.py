from django.urls import path
from .views import CreateMessagesView, ListMessagesView, MessagesDetailView

urlpatterns = [
    path('messages/create/', CreateMessagesView.as_view()),
    path('messages/list/<int:pk>/', ListMessagesView.as_view()),
    path('messages/single/<int:pk>/', MessagesDetailView.as_view())
]