from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys
project = Queue()


def process(path_file, instance):
    file = txt_importer(path_file)
    for el in instance.queue:
        if path_file == el["nome_do_arquivo"]:
            return

    new_format = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(new_format)
    print(new_format)


def remove(instance: Queue):
    response = instance.dequeue()
    if response is None:
        return print("Não há elementos")
    return print(f'Arquivo {response["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance: Queue, position):
    try:
        return print(instance.search(position))
    except IndexError:
        return print("Posição inválida", file=sys.stderr)


process("statics/arquivo_teste.txt", project)
