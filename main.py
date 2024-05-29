def main():
  file_contents = book_text("/home/jahanvi/workspace/github.com/jahanvi513/Bookbot/books/frankenstein.txt")
  words_count = number_of_words(file_contents)
  letter_count = number_of_letters(file_contents)
  letters_dict = sorted_dict(letter_count)
  
  print("---Begin report of books/frankenstein.txt---")
  print(f"{words_count} words found in the document")
  print()
  for item in letters_dict:
    if not item["char"].isalpha():
      continue
    print(f"The '{item['char']} character was found {item['num']} times")
  print("---End Report---")
  

#Function to get the text of the book
def book_text(path):
  with open(path) as f:
    return f.read()

#Function to count number of words in the book
def number_of_words(text):
  words = text.split()
  return len(words)

#Function to count number of letters in the book
def number_of_letters(text):
  letters = {}
  text = text.lower()
  
  for str in text:
    if str in letters:
      letters[str] += 1
    else:
      letters[str] = 1
  return letters

#Function to return the num value of letters dictionary
def sort(letters):
  return letters["num"]

#Function to sort letters dictionary
def sorted_dict(letter_count):
  sorted = []
  for char in letter_count:
    sorted.append({"char": char, "num": letter_count[char]})
  sorted.sort(reverse=True, key=sort)
  return sorted
  
main()
  
  