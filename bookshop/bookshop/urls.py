
from django.contrib import admin
from django.urls import path

# image work 
from django.conf.urls.static import static
from django.conf import settings
from ecom import admin_view
from ecom import views
urlpatterns = [
    # public urls
    path('', views.homepage, name="homepage"),
    path('/add-to-cart/<int:book_id>/', views.addToCart, name="addToCart"),
    path('/remove-from-cart/<int:book_id>/', views.removeFromCart, name="removeFromCart"),
    path('accounts/login/', views.login, name="login"),
    path('accounts/logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('genre/filter/<int:genre_id>/', views.filterByGenre, name="filterByGenre"),
    path('book/<int:book_id>/', views.bookDetails, name="bookDetails"),
    path('cart/', views.cart, name="cart"),
    
    # admin urls
    path('admin/', admin.site.urls),
    
    # superadmin urls
    path("superadmin/", admin_view.admin_dashboard, name="admin_dashboard"),
    path("superadmin/book/insert", admin_view.insert_book, name="insert_book"),
    path("superadmin/book/delete/<int:id>/", admin_view.delete_book, name="delete_book"),
    path("superadmin/genre/insert", admin_view.insert_genre, name="insert_genre"),
    path("superadmin/genre/delete/<int:id>/", admin_view.delete_genre, name="delete_genre"),
    path("superadmin/genre/", admin_view.manage_genre, name="manage_genre"),
    path("superadmin/books/", admin_view.manage_books, name="manage_books"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)