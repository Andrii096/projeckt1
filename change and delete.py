@input_error
def change_info(name, attribute, new_value):
    if name not in data:
        return "Name not found in contacts!"
    else:
        if attribute == "phone":
            data[name]["phone"] = new_value
            return f"Phone number for '{name}' has been changed to '{new_value}'."
        elif attribute == "email":
            data[name]["email"] = new_value
            return f"Email for '{name}' has been changed to '{new_value}'."
        elif attribute == "birthday":
            data[name]["birthday"] = new_value
            return f"Birthday for '{name}' changed to '{new_value}'."


@input_error
def delete_info(name, attribute):
    if name not in data:
        return "Name not found in contacts!"
    else:
        if attribute == "phone":
            del data[name]["phone"]
            return f"The phone number for '{name}' has been deleted."
        elif attribute == "email":
            del data[name]["email"]
            return f"Email for '{name}' has been deleted."
        elif attribute == "birthday":
            del data[name]["birthday"]
            return f"Birthday for '{name}' has been deleted."

def my_help():

            "change name attribute new_value\n"  # Додано команду для зміни
            "delete name attribute\n"  # Додано команду для видалення

            )


commands = {
    "change": change_info,  # Додано команду для зміни
    "delete": delete_info,  # Додано команду для видалення
}