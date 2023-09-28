import sys


def txt_importer(path_file):
    if path_file[-3:] == "txt":
        try:
            with open(path_file, mode="r", encoding="UTF-8") as file:
                content = file.read().split("\n")
                return content
        except FileNotFoundError:
            error_message = f"Arquivo {path_file} não encontrado"
            return print(error_message, file=sys.stderr)
    return print("Formato inválido", file=sys.stderr)
# push
