from django.contrib.auth.models import Permission, User
from guardian.shortcuts import assign_perm, remove_perm


def grant_editor_status(user_object):
    add_perm = Permission.objects.get(name='Can add books')
    change_perm = Permission.objects.get(name='Can change books')
    delete_perm = Permission.objects.get(name='Can delete books')

    user_object.user_permission.add(add_perm, change_perm, delete_perm)
    return User.objects.get(id=user_object.id)


def grant_deletion_status(user_object):
    delete_perm = Permission.objects.get(name='Can delete books')
    user_object.user_permission.add(delete_perm)
    return User.objects.get(id=user_object.id)


def assign_object_delete_perm(user_object, instance):
    assign_perm('delete_books', user_object, instance)
    return User.objects.get(id=user_object.id)


def revoke_object_view_perm(user_object, instance):
    remove_perm('view_articles', user_object, instance)
    return User.objects.get(id=user_object.id)
