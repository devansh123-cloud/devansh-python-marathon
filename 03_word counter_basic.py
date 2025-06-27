#function for count word
def count_words(text):
    words = text.split()
    return len(words)  # ✅ Return the word count

#text
text = input("Enter your text: ")
count = count_words(text)
print("Word Count:", count)

