from django.contrib import admin


# # 사용자 밑에 프로필 보여주기 위함
# class ProfileInLine(admin.StackedInline):
#     model = Profile
#     con_delete = False # 프로필 삭제

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInLine)


# admin.site.register(Profile)