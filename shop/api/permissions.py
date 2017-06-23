from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the seller of this product."
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user.seller