def change_note():
    if not notes:
        print("Немає доступних нотаток для зміни.")
        return

    view_notes()
    choice = int(input("\nВиберіть номер нотатки, яку ви хочете змінити: "))
    if choice < 1 or choice > len(notes):
        print("Некоректний номер нотатки.")
        return

    note_to_change = notes[choice - 1]
    print(f"Ви обрали нотатку з заголовком '{note_to_change['title']}' для зміни.")
    
    new_title = input("Введіть новий заголовок нотатки (натисніть Enter, щоб залишити без змін): ")
    if new_title:
        note_to_change['title'] = new_title

    new_content = input("Введіть новий текст нотатки (натисніть Enter, щоб залишити без змін): ")
    if new_content:
        note_to_change['content'] = new_content

    new_tags = input("Введіть нові теги (розділіть їх комами) (натисніть Enter, щоб залишити без змін): ")
    if new_tags:
        note_to_change['tags'] = new_tags.split(', ')

    print("Нотатка успішно змінена!")

def delete_note():
    if not notes:
        print("Немає доступних нотаток для видалення.")
        return

    view_notes()
    choice = int(input("\nВиберіть номер нотатки, яку ви хочете видалити: "))
    if choice < 1 or choice > len(notes):
        print("Некоректний номер нотатки.")
        return

    deleted_note = notes.pop(choice - 1)
    print(f"Нотатка з заголовком '{deleted_note['title']}' була успішно видалена.")

def main():
    while True:
        print("\n1. Додати нотатку")
        print("2. Переглянути нотатки")
        print("3. Пошук за тегом")
        print("4. Змінити нотатку")
        print("5. Видалити нотатку")
        print("6. Вийти")

        choice = input("\nВиберіть опцію: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_by_tag()
        elif choice == '4':
            change_note()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            print("До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()