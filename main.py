def main():
    book_path = './books/frankenstein.txt'
    text = get_book_text(book_path)

    num_words = count_words(text)
    num_characters = count_characters(text)

    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words in the doc.')
    print()
    for key, value in num_characters.items():
        if not key.isalpha(): # check if char is in the alphabet
            continue
        print(f'The {key} character was found {value} times')

def count_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    text_joined = " ".join(text).lower()
    char_dict = {}
    for char in text_joined.split():
        if char not in char_dict.keys():
            char_dict[char] = 1
        char_dict[char] += 1
    # sort the dict by it's values
    return dict(sorted(char_dict.items(), reverse=True, key=lambda item: item[1]))


if __name__ == '__main__':
    main()