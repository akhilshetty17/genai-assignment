#Text Analysis Functions
#Count number of words
def count_words(text):
    words = text.split()
    return len(words)
#Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count
#Count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count = count + 1
    return count

#Reverse text
def reverse_text(text):
    return text[::-1]

#Check if palindrome
def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]
#Remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result = result + char
    return result
#Word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq
#Longest word
def longest_word(text):
    words = text.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
def analyze_text():
    user_input = input("Enter text to analyze:")
    print("==========TEXT ANALYSIS==========")
    print("Words:",count_words(user_input))
    print("Vowels:",count_vowels(user_input))
    print("Consonants:",count_consonants(user_input))
    print("Reversed:",reverse_text(user_input))
    print("Palindrome:","Yes" if is_palindrome(user_input) else "No")
    print("Without Vowels:",remove_vowels(user_input))
    lw = longest_word(user_input)
    print("Longest Word:", lw, "(" + str(len(lw)) + " letters)")
    print("Word Frequency:", word_frequency(user_input))
analyze_text()