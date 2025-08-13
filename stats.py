def get_num_words(text):
    num_words = text.split()
    return len(num_words)


def get_chars_dict(text):
    character_frequency = {}
    for char in text:
        lowered = char.lower()
        if lowered in character_frequency:
            character_frequency[lowered] += 1
        else:
            character_frequency[lowered] = 1
    return character_frequency


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list