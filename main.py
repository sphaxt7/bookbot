def main():
    file_path = "books/frankenstein.txt" 
    text = get_text(file_path)
    num_words = get_words(text)
    char_dict = get_chars_dict(text)
    sorted_chars = get_sorted_chars(char_dict)
    output(file_path, num_words, sorted_chars)


def output(book ,words, chars):
    print(f"---- Book Report of {book} ----")
    print(f"{words} words found in the book")
    print()

    for char in chars:
        print(f"The character '{char["char"]}' was found {char["num"]} times in the book")

    print("\n \t ------- End of Report --------")



def get_sorted_chars(dict):
    sorted_list = []
    for char in dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": dict[char]})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
        
    return sorted_list



def get_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
    
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


if __name__ == "__main__":
    main()


