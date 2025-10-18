from django.urls import path
from . import views

urlpatterns = [
    path('books', views.manage_books),
    path('books/<int:id>', views.manage_book),
    path('books/search', views.search_books_by_category),
    path('books/low-stock', views.low_stock_books),
    path('books/<int:id>/calculate-price', views.calculate_price)
]