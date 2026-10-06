def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

text = input("Enter a word or sentence: ")
print("It is a palindrome." if is_palindrome(text) else "It is not a palindrome.")
