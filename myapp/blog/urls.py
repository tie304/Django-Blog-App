from django.urls import path, include

from .views import post_list, post_detail, user, user_like


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('post/', post_list),
    path('post/<int:pk>/', post_detail),
    path('user/<int:pk>', user),
    path('user/like/<int:post_key>/<int:user_id>', user_like)
]