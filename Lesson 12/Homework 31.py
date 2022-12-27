import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """удаляет из текста html теги и пустые строки"""

    # Находим начало и конец тега, и заменяем с помощью срезов теги на пустые строки
    with codecs.open(html_file, 'r', 'utf-8') as html:
        edit_text = html.read()
        while edit_text.find('<') >= 0:
            start_symbol = edit_text.find('<')
            end_symbol = edit_text.find('>')
            tag = edit_text[start_symbol:end_symbol + 1]
            edit_text = edit_text.replace(tag, '')
        html.close()

    # Записываем текст без тегов в документ txt
    with codecs.open('cleaned.txt', 'w', 'utf-8') as result_text:
        result_text.write(edit_text)

    # Перезаписываем документ txt, удаляя пустые строки
    result_text = codecs.open('cleaned.txt', 'r', 'utf-8')
    edit_text = ''
    for line in result_text:
        is_only_spaces = True
        for i in line:
            # Проверяю, содержит ли строка что-либо, кроме пробелов или переноса строки
            if i != ' ' and i != '\n':
                is_only_spaces = False
                break
        if not is_only_spaces:
            edit_text += line
    result_text.close()

    with codecs.open('cleaned.txt', 'w', 'utf-8') as result_text:
        result_text.write(edit_text)


delete_html_tags('draft.html')
