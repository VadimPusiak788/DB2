from rest_framework import generics
from .models import ChatModel
from .serializers import CreatePostSerializers, ListPostSerializers


class CreateMessagesView(generics.CreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = CreatePostSerializers


class ListMessagesView(generics.ListAPIView):
    serializer_class = ListPostSerializers

    def get_queryset(self):
        number = self.kwargs['pk']
        delta = 10
        if number == 0:
            return ChatModel.objects.all()[:delta]
        return ChatModel.objects.all()[number*delta:(number+1)*delta]


class MessagesDetailView(generics.RetrieveAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ListPostSerializers
