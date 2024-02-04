# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
    list1 = [*string1.replace(' ', '').lower()]
    list2 = [*string2.replace(' ', '').lower()]
    
    if len(list1) != len(list2):
        return False
    else:
        chars_found = 0
        for char in list1:
            if list2.index(char) >= 0:
                chars_found += 1
        if chars_found == len(list1):
            return True
        else:
            return False
            


# Part 2
list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
def anagrams_for(word, list_of_words):
    anagrams = []
    for curr in list_of_words:
        if is_character_match(word, curr) == True:
            anagrams.append(curr)
    return anagrams

print(anagrams_for("threads", list_of_words))