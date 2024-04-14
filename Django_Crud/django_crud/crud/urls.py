from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),
    path('home/',home),
    path('crud_add/',crud_add),
    path('crud_delete/<int:id>',crud_delete),
    path('crud_edit/<int:id>',crud_edit),
    path('crud_update/<int:id>',crud_update),




]
