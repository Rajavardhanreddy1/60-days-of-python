def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        # Sort the word to get the key
        sorted_word = ''.join(sorted(word))
        
        # Group words by their sorted key
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    # Return the values (list of anagram groups)
    return list(anagram_dict.values())

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
