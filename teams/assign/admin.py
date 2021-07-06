from django.contrib import admin
from .models import Person, Team, Relation#, Group 

from django.contrib.admin import DateFieldListFilter
from  rangefilter.filters  import  DateRangeFilter ,  DateTimeRangeFilter


from django.contrib import admin

#from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

"""
class UserProfileInline(admin.StackedInline):
 model = UserProfile
 max_num = 1
 can_delete = False
"""





class TeamInlineAdmin(admin.TabularInline):
    model = Team.users.through


class TeamAdmin(admin.ModelAdmin):
    model = Team
    readonly_fields = ('thumbnail_preview',)
    list_display = ('name', 'get_users',"thumbnail")    
    fieldsets = (
        (None, {'fields': ('name',"thumbnail")}),   #, 'email_to'
    )
    inlines = (TeamInlineAdmin,)


    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    

class PersonAdmin(admin.StackedInline):
 model = Person
 max_num = 1
 can_delete = False

class UserAdmin(AuthUserAdmin):
 inlines = [PersonAdmin]


class RelationAdmin(admin.ModelAdmin): 
    model = Relation 
    list_display = ('team', 'person', "date_joined")
    #filter_horizontal = ('team', 'person', "date_joined")
    list_filter = (('person',admin.RelatedOnlyFieldListFilter),
    	('team',admin.RelatedOnlyFieldListFilter),
    	('date_joined', DateFieldListFilter),
    	( 'date_joined' ,  DateRangeFilter ),
    	)
    search_fields  =  ( "person__nickname" , "team__name", "person__user__email", "person__user__first_name", "person__user__username", "person__user__last_name")

    

"""    
class GroupAdmin(admin.ModelAdmin):  
    model = Group

    
class GroupAdmin(admin.ModelAdmin):
    model = Group
    inlines = [UserAdmin, TeamAdmin]
"""


#admin.site.register(User)
#admin.site.register(Team)

#admin.site.register(Person, PersonAdmin)
# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin) 
admin.site.register(Team, TeamAdmin)

admin.site.register(Relation, RelationAdmin)
#admin.site.register(Group, GroupAdmin)

"""

class EmailGroupAdmin(ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'email_to')}),
    )
    filter_horizontal = ('email_to',)
"""

