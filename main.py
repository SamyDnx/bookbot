import sys
from stats import get_num_words, get_num_letters, list_dict

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    txt = get_book_text(sys.argv[1])
    cnt = get_num_words(txt)
    dic = get_num_letters(txt)
    ls = list_dict(dic)
    
    pretty_print(cnt, ls)

def get_book_text(path):
    with open(path, "r") as f:
        text = f.read()
    
    return text

def pretty_print(cnt, ls):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {cnt} total words")
    print("--------- Character Count -------")
    
    for dic in ls:
        val = list(dic.values())
        if val[0].isalpha():
            print(f"{val[0]}: {val[1]}")
    
    print("============= END ===============")


main()