import sys
from ting_file_management.file_management import txt_importer


def verify_file_exist(path_file, instance):
    for index in range(len(instance.items)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return True


def process(path_file, instance):
    if not verify_file_exist(path_file, instance):
        qty_lines = len(txt_importer(path_file))
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": qty_lines,
            "linhas_do_arquivo": txt_importer(path_file),
        }
        instance.enqueue(file)
        sys.stdout.write(str(file))


def remove(instance):
    if len(instance.items) != 0:
        delete_file = instance.dequeue()
        file_name = delete_file["nome_do_arquivo"]
        print(f'Arquivo {file_name} removido com sucesso')
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write('Posição inválida')
