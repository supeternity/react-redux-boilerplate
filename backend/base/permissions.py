from rest_framework import permissions


class ClientAccessPermission(permissions.IsAdminUser):
    pass
