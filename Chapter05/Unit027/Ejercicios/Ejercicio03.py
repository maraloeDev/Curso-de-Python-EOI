def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram("listen", "silent"))     # True
print(is_anagram("anagram", "nagaram"))   # True
print(is_anagram("listen", "silence"))   # False
print(is_anagram("anagram", "anagrams"))  # False