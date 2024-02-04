from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as DjangoGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from user.models import UserBase


@admin.register(UserBase)
class AccountAdmin(BaseUserAdmin):

    fieldsets = (
        ('Account Information', {"fields": ('email', 'username', 'password', 'first_name','last_name','slug')}),
        ('Permissions', {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), "classes": ('collapse',)}),
        ('Important dates', {'fields': ('last_login',), "classes": ('collapse',)})
    )

    list_display = ('username', 'email',  'id', 'is_staff', 'is_active', 'last_login' )
    list_filter = ['is_active', 'is_staff', 'groups']
    search_fields = ['email', 'username', 'id', 'slug']


class GroupAdminForm(forms.ModelForm):
    """
    ModelForm that adds an additional multiple select field for managing
    the users in the group.
    """
    users = forms.ModelMultipleChoiceField(
        UserBase.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Users', False),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            initial_users = self.instance.user_set.values_list('pk', flat=True)
            self.initial['users'] = initial_users


    def save(self, *args, **kwargs):
        kwargs['commit'] = True
        return super(GroupAdminForm, self).save(*args, **kwargs)


    def save_m2m(self):
        self.instance.user_set.clear()
        self.instance.user_set.add(*self.cleaned_data['users'])

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(DjangoGroupAdmin):
    """
    Customized GroupAdmin class that uses the customized form to allow
    management of users within a group.
    """
    form = GroupAdminForm