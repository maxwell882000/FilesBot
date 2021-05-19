from django.urls import path
from .views import index, categories, files, settings, bot, statistics, botusers
from FileTelegramBot.settings import WEBHOOK_URL_PATH

urlpatterns = [
    path('', index.IndexView.as_view(), name='admin-home'),
    path('catalog/', categories.CategoryListView.as_view(), name='admin-catalog'),
    path('settings/', settings.SettingsView.as_view(), name='admin-settings'),
    path('settings/send-advertising-post', settings.AdvertisingPostView.as_view(), name='admin-settings-advertising-post'),
    path('catalog/<int:pk>', categories.ShowCategoryChildrenView.as_view(), name='admin-catalog-categories-children'),
    path('catalog/<int:pk>/files', categories.ShowCategoryFilesView.as_view(), name='admin-catalog-categories-files'),
    path('catalog/category/add', categories.CreateCategoryView.as_view(), name='admin-catalog-category-add'),
    path('catalog/category/<int:pk>/edit', categories.UpdateCategoryView.as_view(), name='admin-catalog-category-edit'),
    path('catalog/category/<int:pk>/remove', categories.DeleteCategoryView.as_view(), name='admin-catalog-category-remove'),
    path('catalog/files/add', files.CreateFileView.as_view(), name='admin-catalog-files-add'),
    path('catalog/files/<int:pk>/edit', files.UpdateFileView.as_view(), name='admin-catalog-files-edit'),
    path('catalog/files/<int:pk>/remove', files.DeleteFileView.as_view(), name='admin-catalog-files-remove'),
    path('statistics/', statistics.StatisticsIndexView.as_view(), name='admin-statistics'),
    path('bot-users/', botusers.BotUsersIndexView.as_view(), name='admin-botusers'),
    path('catalog/user-files/', files.UserFilesView.as_view(), name='admin-catalog-userfiles'),
    path('catalog/user-files/<int:pk>/confirm', files.ConfirmUserFileView.as_view(), name='admin-catalog-userfiles-confirm'),

    path('init/', bot.BotInitializeView.as_view()),
    path(WEBHOOK_URL_PATH, bot.BotUpdatesRecieverView.as_view())
]