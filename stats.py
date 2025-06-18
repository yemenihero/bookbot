
def count(text):
    words = text.split()
    return len(words)

def letters(content)    :
    letters_dic ={}                                           
    for i in content.lower() :
        if i in letters_dic:
            letters_dic[i] += 1
        else : 
            letters_dic[i] = 1
    return letters_dic                                              
        
#if you use  : #bookpath = "books/frankenstein.txt" 
               #with open(bookpath) as f : 
                 # content = f.read() 
# instade of letters(content) , you must remove content argament in the function , and also remove it from main.py
def sort_on(dic_item):
    return dic_item["num"]

def chars_dic_to_sort_list(letters_dic):
    letters_list = []
    for character in letters_dic :
        if character.isalpha() :
            letters_list.append({"char":character , "num":letters_dic[character]})
    letters_list.sort(reverse=True , key = sort_on)
    return letters_list