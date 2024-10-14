def format_name(first_name, last_name):
    """
    Take the first name and last name and format it to return the title case version of the name.

    :param first_name: first name of the user
    :param last_name: last name of the user
    :return: title case version of the name
    """
    if first_name == "" or last_name == "":
        return "You did not provide valid inputs"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Result: {formatted_first_name} {formatted_last_name}"


print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
