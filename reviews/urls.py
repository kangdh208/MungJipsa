from django.urls import path
from . import views
# Create your views here.

app_name ='reviews'
urlpatterns = [
    # 멍스타그렘
    path('', views.index, name='index'),

    # 리뷰작성 
    path('create/', views.create, name='create'),
    
    #리뷰 수정
    path('<int:pk>/update/', views.update, name='update'),

    # 리뷰 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 댓글 작성
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    
    # 댓글 삭제
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name ='comment_delete'),

    # 해시태그
    path('hashtag/', views.hashtag, name="hashtag"),

]