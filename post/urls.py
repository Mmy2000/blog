from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:id>',views.post_details,name='post_details'),
    path('create',views.post_create , name='post_create'),
    path('<int:id>/edit',views.post_edit,name='Post_edit'),
    path('cbv' , views.PostList.as_view() , name='post_list_cbv'),
    path('cbv/create' , views.PostCreate.as_view() , name='post_create_cbv'),
    path('cbv/<int:pk>' , views.PostDetails.as_view() , name='post_detail_cbv'),
    path('cbv/<int:pk>/edit' , views.UpdateView.as_view() , name='post_update_cbv'),

]