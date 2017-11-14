from django.contrib import admin

from onlinetest.models import TestDetails, StudentProfile, Question, studentMark, clientsTable
# Register your models here.

admin.site.register(TestDetails)
admin.site.register(StudentProfile)
admin.site.register(Question)
admin.site.register(studentMark)
admin.site.register(clientsTable)


