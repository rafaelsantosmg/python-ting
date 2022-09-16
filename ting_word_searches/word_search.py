def exists_word(word, instance):
    list_words = []
    ocorrencies = []

    for item in range(len(instance.items)):
        for i, line in enumerate(instance.search(item)["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencies.append({"linha": i + 1})

        file_name = instance.search(item)["nome_do_arquivo"]
        if len(ocorrencies) != 0:
            list_words.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": ocorrencies,
            })
    return list_words


def search_by_word(word, instance):
    pass
