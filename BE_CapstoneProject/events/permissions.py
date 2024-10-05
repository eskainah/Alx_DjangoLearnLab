from rest_framework import permissions

#Custom permission to only allow owners of an event to edit or delete it.
class IsEventOwner(permissions.BasePermission):
    
    # allow owners to update or delete the event
    def has_object_permission(self, request, view, obj):
       
        return obj.organizer == request.user
    # Allow authenticated users to list or create events
    def has_permission(self, request, view):
       
        return request.user and request.user.is_authenticated
