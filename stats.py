def get_num_words(text: str) -> int:
    num_words = text.split()
    return len(num_words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict


def sort_on(d: dict) -> int:
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list:
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list