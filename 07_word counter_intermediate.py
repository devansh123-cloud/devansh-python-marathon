# This Python script is a word counter program that takes input from the user, analyzes the text, and
# then displays various statistics about the input text. Here's a breakdown of what the script does:
import sys
print("📄 Word Counter Intermediate Version")
print("✍️ Enter your text below (press Ctrl+Z + Enter on Windows OR Ctrl+D on Mac/Linux to finish):\n")

# Accept multiline input
text = sys.stdin.read()

# Count features
char_count = len(text)
word_count = len(text.split())
sentence_count = text.count(".") + text.count("!") + text.count("?") + text.count(".")
paragraph_count = len(text.strip().split("\n\n"))

# Display the results
print("\n✅ Text Analysis:")
print("----------------------------")
print(f"Characters:  {char_count}")
print(f"Words:       {word_count}")
print(f"Sentences:   {sentence_count}")
print(f"Paragraphs:  {paragraph_count}")
print("----------------------------")

