from django.contrib import admin
from django.urls import include, path

""" Django管理サイト名変更"""
admin.site.site_header = 'Djangoカスタムサイト'

""" サイト管理名変更"""
admin.site.index_title = 'モデルリスト'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]