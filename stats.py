def count_words(text):
    words = text.split()
    return len(words)
def count_chars(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return(chars)
def sort_char_counts(char_count):
    def sort_on(dict):
        return dict["num"]
    sorted_char_counts = []
    for key in char_count:
        char_dict = {
            "char": key,
            "num": char_count[key]
        }
        sorted_char_counts.append(char_dict)
    sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts
        

