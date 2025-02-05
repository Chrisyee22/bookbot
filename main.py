path = "books/frankenstein.txt"

def count_words():
    with open(path) as f:
        file_contents = f.read()
        count = 0
        for word in file_contents.split():
            count += 1
        return count


def count_char():
    with open(path) as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        char_count = {}
        for char in lower_case:
            # check if variable for character exists
            if char in char_count:
                # if it does, increment the count by 1
                char_count[char] += 1
            else:
                char_count[char] = 1
            
        return char_count    

#count_char()

def sort_on(dict):
    return dict["num"]

def only_letters():
    char_count = count_char()
    char_list = [
        {"char": char, "num": count}
        for char, count in char_count.items()
    ]
    
    char_list.sort(reverse=True, key=sort_on)
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The {char_dict['char']} characater appears {char_dict['num']} times")

print(f"---Begin report of {path} ---")
print(f"{count_words()} words found in the document")
only_letters()
print("---End report ---")