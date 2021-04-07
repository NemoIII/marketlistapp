from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='items'),
    path('item/<int:pk>', TaskDetail.as_view(), name='item'),
    path('item-create/', TaskCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>', TaskUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>', TaskDelete.as_view(), name='item-delete'),
]
