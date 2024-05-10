from rest_framework import permissions

class IsSecretKeyCorrect(permissions.BasePermission):
    message = '당신은 접근할 수 없습니다.'

    def has_permission(self, request, view):
        return request.headers.get('Secret-Key') == "this_is_secret_key"


class IsOwnerOrReadOnly(IsSecretKeyCorrect):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.writer == request.user
