from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views

urlpatterns = [
    path('user/token/', api_views.MyTokenObtainaPairView.as_view()),
    path('user/token/referesh', TokenRefreshView.as_view()),
    path('user/register/', api_views.RegisterView.as_view()),
    path('user/profile/<user_id>', api_views.ProfileView.as_view()),

    #POST ENDPOINTS
    path('post/category/list/', api_views.CategoryListApiView.as_view()),
    path('post/category/posts/<category_slug>/', api_views.PostCategoryListApiView.as_view()),
    path('post/lists/', api_views.PostListApiView.as_view()),
    path('post/detail/<slug>/', api_views.PostDetailApiView.as_view()),
    path('post/like-post/', api_views.LikePostApiView.as_view()),
    path('post/comment-post/', api_views.PostCommentApiView.as_view()),
    path('post/bookmark-post/', api_views.BookmarkPostApiView.as_view()),

]