text = input("Enter your feedback: ")

bad_words = ["bad", "hate", "stupid"]

for word in bad_words:
    text = text.replace(word, "****")

print("Filtered Feedback:", text)
