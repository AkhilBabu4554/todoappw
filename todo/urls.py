from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.task_view,name=('TaskList')),
    path('create/',views.create_view,name=('Create')),
    path('update/<int:id>/',views.update_view,name=('Update')),
    path('delete/<int:id>/',views.deleteview,name=('Delete')),
    path('toggle/<int:id>/',views.Toggleview,name=('Toggle')),
    path('Register/',views.RegisterView,name=('Register')),
    path('login/',views.loginview,name=('login')),
    path('logout/',views.logoutview,name=('logout')),
]
