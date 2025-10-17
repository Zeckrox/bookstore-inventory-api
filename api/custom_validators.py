from django.core.exceptions import ValidationError

def validate_isbn(isbn):
    allowed_lengths = [10, 13]  # Formatos validos
    numbers = []
    for i in isbn:
        if i.isnumeric():
            numbers.append(int(i))
    if len(numbers) not in allowed_lengths:
        raise ValidationError(("Formato incorrecto para el isbn"))