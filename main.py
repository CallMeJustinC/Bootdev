def main():
    book_path = "github.com/CallMeJustinC/bookbot/books/frankenstein.txt"
    book_frank = get_book_text(book_path)
    number_of_words = count_words(book_frank)
    number_of_characters = count_characters(book_frank)
    chars_sorted_list = chars_dict_to_sorted_list(number_of_characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha(): 
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(book_path):
    with open("github.com/CallMeJustinC/bookbot/books/frankenstein.txt") as frank:
        return frank.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(book_frank):
    lowered = book_frank.lower()
    characters = {}    
    for character in lowered:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(c):
    return c["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()