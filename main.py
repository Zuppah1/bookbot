def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_letters_list(text)
    dictionary = get_dictionary(letters)
    d_list = list_of_dictionaries(dictionary)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for item in d_list:
        print(f"The '{item["letter"]}' character was found {item["num"]} times")

    print("--- End report ---")
    


# Splitting the words string into string list and returning length to count word amount

def get_num_words(text):
    words = text.split()
    return len(words)

# Opening text file and asigning the string to a variable

def get_book_text(path):
    with open(path) as f:
        return f.read()

# Splitting the text string into a symbol list

def get_letters_list(text):
    letters = list(text)
    return letters

# Creating a symbol dictionary with occurance times

def get_dictionary(letters):
    count = {}
    for letter in letters:
        lowered = letter.lower()
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count

# Creating a list of dictionaries with only letter symbols and their values

def list_of_dictionaries(dictionary):
    d_list = []
    for letter, value in dictionary.items():
        if letter.isalpha() == True:
            new_dict = {
                "letter": letter, 
                "num": value
            }
            d_list.append(new_dict)
    d_list.sort(reverse=True, key=sort_on)
    return d_list

def sort_on(d_list):
    return d_list["num"]


    
main()