from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('add/<str:name>', views.add, name='add'),
    path('view_employees', views.view_employees, name='view_employees'),
    path('view_departments', views.view_departments, name='view_departments'),
    path('view_roles', views.view_roles, name='view_roles'),
    path('view_budgets', views.view_budgets, name='view_budgets'),
    path('employee/<int:pk>', views.employee, name='employee'),
    path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
    path('department/<int:pk>', views.department, name='department'),
    path('update/<str:name>/<int:pk>/', views.update, name='update'),
    path('delete_department/<int:pk>', views.delete_department, name='delete_department'),
    path('role/<int:pk>', views.role, name='role'),
    path('delete_role/<int:pk>', views.delete_role, name='delete_role'),
    path('budget/<int:pk>', views.budget, name='budget'),
    path('department_employees/<int:pk>', views.department_employees, name='department_employees'),
    path('get_department_by_role', views.get_department_by_role, name='get_department_by_role'),
    path('logout', views.logout_user, name='logout')
]