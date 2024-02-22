from collections import OrderedDict

def get_book_text(path):
    with open(path) as filepath:
        return filepath.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count.keys():
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def generate_report_dictionary(dictionary):
    report_list = sort_report_list(dictionary)
    report_dictionary = OrderedDict()
    for i in range(len(report_list)):
        current_dictionary = report_list[i]
        report_dictionary[current_dictionary["num"]] = current_dictionary["char"]
    return report_dictionary


def sort_on(dictionary):
    return dictionary["num"]

def sort_report_list(dictionary):
    report_dictionary_list = []
    for key in dictionary:
        if key.isalpha():
            report_dictionary_list.append({"num":dictionary[key], "char":key})
    report_dictionary_list.sort(reverse=True,key=sort_on)
    return report_dictionary_list

def generate_report(filepath):
    filepath = filepath
    file_contents = get_book_text(filepath)
    word_count = get_word_count(file_contents)
    report_dictionary = generate_report_dictionary(count_characters(file_contents))
    print(report_dictionary)
    report = "--Begin Report on" + filepath + "--\nThis book has " + str(word_count)  + " words.\n\n"
    for key in report_dictionary:
        report += "The char " + report_dictionary[key]+ " was found " + str(key) + " times.\n" 
    return report

def main():
    filepath = "books/frankenstein.txt"
    print(generate_report(filepath))
    
if __name__ == "__main__":
    main()