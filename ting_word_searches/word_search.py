from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    response = list()
    ocorrencia = list()
    for el in instance.queue:
        for ind in range(len(el["linhas_do_arquivo"])):
            if word.lower() in el['linhas_do_arquivo'][ind].lower():
                ocorrencia.append({'linha': ind + 1})
        if len(ocorrencia) > 0:
            response.append({
                "palavra": word,
                "arquivo": el['nome_do_arquivo'],
                "ocorrencias": ocorrencia})
    return response


def search_by_word(word, instance):
    response = list()
    ocorrencia = list()
    for el in instance.queue:
        for ind in range(len(el["linhas_do_arquivo"])):
            if word.lower() in el['linhas_do_arquivo'][ind].lower():
                ocorrencia.append({'linha': ind + 1,
                                   'conteudo': el['linhas_do_arquivo'][ind]})
        if len(ocorrencia) > 0:
            response.append({
                "palavra": word,
                "arquivo": el['nome_do_arquivo'],
                "ocorrencias": ocorrencia})
    return response
