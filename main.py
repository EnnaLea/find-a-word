def found(str1, str2):
    count_word = 0
    for i in str1:
        search_word = str2.find(i)
        if search_word > -1:
            count_word += 1
    if count_word == len(str1):
        return "yes"
    else:
        return "no"

# alternate function
# def found(str1, str2):
#     return "yes" if all(i in str2 for i in str1) else "no"

text1 = input("Enter word to find: ")
text2 = input("Enter a string to search within: ")

result = found(text1, text2)
print(result)