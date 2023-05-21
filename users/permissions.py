from rest_framework import permissions

class CustomReadOnly(permissons.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissons.SAFE_METHODS:
      return True
    return obj.user == request.user