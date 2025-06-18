import sys
from stats import count, letters , chars_dic_to_sort_list




def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    content = get_book_text(bookpath)
    num_words = count(content)
      
    char = letters(content)
    
    char_list = chars_dic_to_sort_list(char)
    
    print_report(bookpath,num_words,char_list)


   
    
    
       
def get_book_text (path):
    try :
        with open(path) as f :                      
            return f.read()   
    except FileNotFoundError :
         print(f"Error: Could not find the file {path}")
         sys.exit(1)
            
def print_report(bookpath,num_words,char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words" )
    print("--------- Character Count -------")
    for i in char_list:
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")


 
main()

