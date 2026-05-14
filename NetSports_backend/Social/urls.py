from django.urls import path

from Social.views import ContentView, MyContentView, LikeView, CommentView, FavouriteView, NotificationListView, \
    ReadNotificationView, UnreadNotificationCountView, MarkAllNotificationsReadView, MyContentListView

urlpatterns = [
    path('content/', ContentView.as_view()),
    path('content/my-contents/', MyContentListView.as_view()),
    path('content/<int:content_id>/', MyContentView.as_view()),
    path('likes/content/<int:content_id>/', LikeView.as_view(), name='like'),
    path('comments/content/<int:content_id>/', CommentView.as_view(), name='comments'),
    path('comments/content/<int:content_id>/comment/<int:comment_id>/', CommentView.as_view(), name='comment'),
    path('favourites/content/<int:content_id>/', FavouriteView.as_view(), name='favourite'),
    path('favourites/my-favourites/', FavouriteView.as_view(), {'action': 'get_user_favourites'}, name='my_favourites'),
    path('notifications/', NotificationListView.as_view()),
    # path('notifications/<int:notification_id>/', ReadNotificationView.as_view()),
    path('notifications/unread-count/', UnreadNotificationCountView.as_view()),
    path('notifications/read-all/', MarkAllNotificationsReadView.as_view())
]