from django.urls import path, include

from .views import posts, post_detail, users, user_like


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('post/', posts),
    path('post/<int:pk>/', post_detail),
    path('user/<int:pk>', users),
    path('user/like/<int:post_id>/<int:user_id>', user_like)
]