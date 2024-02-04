from character_match import is_character_match, anagrams_for
import pytest

# Part 1
def test_is_character_match():
    assert is_character_match('charm', 'march') == True
    assert is_character_match('zach', 'attack') == False
    assert is_character_match('CharM', 'mARcH') == True
    assert is_character_match('abcde2', 'c2abed') == True
    assert is_character_match('Anna Madrigal', 'A man and a girl') == True

# print(is_character_match('charm', 'march') == True)
# print(is_character_match('zach', 'attack') == False)
# print(is_character_match('CharM', 'mARcH') == True)
# print(is_character_match('abcde2', 'c2abed') == True)

# print("This test is for the challenge quesiton")
# print(is_character_match('Anna Madrigal', 'A man and a girl') == True)

# Part 2
def test_anagrams_for():
    list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
    assert anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"]
    assert anagrams_for("apple", list_of_words) == []

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
