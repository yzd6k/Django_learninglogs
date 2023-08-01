"""定义learning_log的URL模式"""
from django.urls import path,re_path
from . import views
app_name="learning_logs"
urlpatterns = [
    #主页
    re_path(r'^$',views.index,name='index'),

    #显示所有的主题
    re_path(r'^topics/$', views.topics, name='topics'),

    #显示特定主题的详细页面
    # re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<entry_id>/',views.edit_entry,name='edit_entry'),
]

