from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError(
            "Você não pode enviar uma imagem maior que 1 Mb, por favor corrija!")
    else:
        return value
