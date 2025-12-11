def get_words_count(text : str) -> int:
 return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
    freq = {}
    for char in text.lower():
        if char.isalpha():  # only count letters a-z
            freq[char] = freq.get(char, 0) + 1
    return freq


def sort_on(items):
    return items["num"]

def sort_dictionary(freq_dict):
 return sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
