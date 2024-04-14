import time

def count_word_occurrences(text):
    """
    Count the occurrences of words in a string.
    """
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_sorted_word_counts(word_counts):
    longest_word_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")


start_time = time.time()

text_input = input("Text: ")
word_counts = count_word_occurrences(text_input)
print_sorted_word_counts(word_counts)

actual_time = time.time() - start_time
print("\nEstimate: 15 minutes")
print(f"Actual: {actual_time:.2f} minutes")