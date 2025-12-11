import sys
from stats import get_words_count, get_char_count, sort_dictionary

def get_book_text(filepath : str):
 with open(filepath) as f:
   return f.read()

def main():
 
 if len(sys.argv) < 2:
   sys.stdout.write("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
 
 text= get_book_text(sys.argv[1])
 num_words= get_words_count(text)
 number_chars = get_char_count(text)

 print(f"Found {num_words} total words")

 sorted_chars = sort_dictionary(number_chars)
 for char, count in sorted_chars:
   print(f"{char}: {count}")

main()
