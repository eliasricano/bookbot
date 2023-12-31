def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_report = get_text_report(chars_dict)
    print(f""" -- Begin report of {book_path} --
        {num_words} words found in the document.
        
        {chars_report}
         -- End Report --""")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1
    return chars

def get_text_report(chars_dictionary):
    dict_to_list = list(chars_dictionary)
    char_list = []
    for c in dict_to_list:
        if c.isalpha():
            char_list.append(c)
    char_list.sort()
    report = []
    for char in char_list:
        report.append(f"The {char} character was found {chars_dictionary[char]}")
    return report
    
main()