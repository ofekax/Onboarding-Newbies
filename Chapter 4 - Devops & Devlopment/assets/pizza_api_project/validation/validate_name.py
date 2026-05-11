from conf import special_characters


def name_doesnt_contain_special_characters(name: str):
    if any(char in special_characters for char in name):
        raise ValueError("name cannot contain special characters")
    return name.title()
