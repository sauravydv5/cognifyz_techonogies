def word_count(filename):
  """Counts the occurrences of each word in a text file.

  Args:
    filename: The name of the text file to process.

  Returns:
    A dictionary containing word counts.
  """

  word_count = {}
  with open(filename, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        word = word.lower()  # Convert words to lowercase for case-insensitive counting
        if word in word_count:
          word_count[word] += 1
        else:
          word_count[word] = 1
  return word_count

def display_word_counts(word_count):
  """Displays the word counts in alphabetical order.

  Args:
    word_count: A dictionary containing word counts.
  """

  sorted_words = sorted(word_count.items())
  for word, count in sorted_words:
    print(f"{word}: {count}")

if __name__ == "__main__":
  filename = input("Enter the filename: ")
  word_count = word_count(filename)
  display_word_counts(word_count)