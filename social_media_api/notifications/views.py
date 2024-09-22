from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class NotificationListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(
            read=False).order_by('-timestamp')
        data = [{'actor': n.actor.username, 'verb': n.verb,
                 'target': str(n.target), 'timestamp': n.timestamp} for n in notifications]
        return Response(data)