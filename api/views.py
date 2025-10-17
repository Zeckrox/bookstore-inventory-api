from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Book
from rest_framework import status
from api.serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(['GET','POST'])
def manage_books(request):
    # Listar todos los libros (con paginación opcional)
    if request.method == "GET":
        books = Book.objects.all()
        # Si se incluyo paginación en la URL, entonces la aplica.
        if request.GET.get("page"):
            pagination_class = PageNumberPagination
            pagination_class.page_size = 2
            paginator = pagination_class()
            books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Crear libro
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def manage_book(request, id):
    # Verifica si existe un libro con ese id.
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener libro por ID
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Actualizar libro
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Eliminar libro
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Buscar por categoría
@api_view(['GET'])
def search_books_by_category(request):
    category = request.GET.get("category")
    # Verifica que se haya enviado el parametro de busqueda.
    if not category: return Response(status=status.HTTP_400_BAD_REQUEST)
    # Eliminamos los corchetes del texto.
    category = category[1:-1] 
    books = Book.objects.filter(category=category)
    # Si no hay libros de esta categoria, se envia un 404.
    if not books.count(): return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Libros con stock bajo
@api_view(['GET'])
def low_stock_books(request):
    threshold = request.GET.get("threshold")
    # Verifica que se haya enviado el parametro de busqueda.
    if not threshold: return Response(status=status.HTTP_400_BAD_REQUEST)

    books = Book.objects.filter(stock_quantity__lte= threshold)
    # Si no hay libros dentro de este rango, se envia un 404.
    if not books.count(): return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)