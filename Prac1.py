
import random 



#___________________________________


def multiplication_table():

   num = int(input("Enter the number: "))

   print("\nMultiplication Table:\n")
   print(f"1 * {num}: {1*num}")
   print(f"2 * {num}: {2*num}")
   print(f"3 * {num}: {3*num}")
   print(f"4 * {num}: {4*num}")
   print(f"5 * {num}: {5*num}")
   print(f"6 * {num}: {6*num}")
   print(f"7 * {num}: {7*num}")
   print(f"8 * {num}: {8*num}")
   print(f"9 * {num}: {9*num}")



#___________________________________

def calculator():
    nr1 = float(input("Enter the first number: "))
    nr2 = float(input("Enter the second number: "))
    oper = input("Enter the operation (+, -, *, /): ")

    if oper == "+":
        print(f"The sum is {nr1 + nr2}")
    elif oper == "-":
        print(f"{nr1} - {nr2}: {nr1 - nr2}")
    elif oper == "*":
         print(f"{nr1} * {nr2}: {nr1 * nr2}")
    elif oper == "/":
         print(f"{nr1} / {nr2}: {nr1 / nr2}")
    else:
        print("\nWrong operation")


#___________________________________


def sum_of_firstn_numbers(num):

   sum = 0

   for i in range(1, num+1):
    sum += i

   print(f"\n{sum}")

#___________________________________

def guess_the_number():

  random_number = random.randint(1,10)

  while(True):
    number = int(input("Enter the number: "))

    if number == random_number:
        print("You guess the number!!!")
        break

#___________________________________ Slice with [start: end: step]

def palindrome_checker():

    word = input("Enter the word: ")
    reverse_word = word[-1::-1]

    if word == reverse_word:
      print("The word is a palindrome!!!")
    else:
      print("The word isn't a palindrome!!!")


def palindrome_checker2():
  word = input("Enter the word: ")
  reverse_word = ""
  
  for i in range(len(word)):
    reverse_word += word[-(i+1)]

  if word == reverse_word:
    print("The word is a palindrome!!!")
  else:
    print("The word isn't a palindrome!!!")


    
#___________________________________

def list_filter():
  index = int(input("Enter the number of elements in the list: "))
  listU = []
  even_list = []

  for i in range(index):
    num = int(input("Enter the number: "))
    listU.append(num)

  for i in range(index):
    if (listU[i] % 2) == 0:
      even_list.append(listU[i])
    
  print(f"Original list: {listU}")
  print(f"Even list: {even_list}")


#___________________________________ Corregir

def word_counter():

  text = input("Enter the text: ")

  list_words = []
  word = ""
  count = 0

  for i in range(len(text)):
    if text[i] != " ":
      word += text[i]
    else: 
      list_words.append(word)
      word = ""
    
  if word:
      list_words.append(word)

  for e in range(len(list_words)):
    for i in range(len(list_words)):
      if list_words[e] == list_words[i]:
        count += 1
    print(f"The word {list_words[e]} appears {count} times.")
    count = 0


def word_counter2():
  text = input("Enter the text: ")
  words = text.split()  # splits by spaces automatically

  for word in set(words):
      print(f"The word '{word}' appears {words.count(word)} times.")

  

#___________________________________

def max_min_average():

  list_numbers = []
  index = int(input("Enter the number of the index for the list: "))
  number = ""
  summ = 0

  for i in range(index):
    number = int(input(f"Enter the {i+1} number: "))
    list_numbers.append(number)
    summ += number
  

  print(f"List: {list_numbers}")
  print(f"Max number: {max(list_numbers)}")
  print(f"Min number: {min(list_numbers)}")
  print(f"Average: {summ/index}")
      



#___________________________________

def fibonacci_sequence():

  number = int(input("Enter the number: "))
  
  if number <= 0:
    print("Enter a positive number")
    return
  elif number == 1:
    print(f"Fibonacci {number}: 0")
    return
  elif number == 2:
    print(f"Fibonacci {number}: 1")
    return
  
  # For numbers > 2, calculate using the sequence
  a, b = 0, 1
  for i in range(3, number + 1):
    a, b = b, a + b
  
  print(f"Fibonacci {number}: {b}")
    
#___________________________________


def word_to_list(word):

  list_w = []

  for i in range(len(word)):
    list_w.append(word[i])

  return list_w


def anagram_checker():  # correct

  word1 = input("Enter the first word: ")
  word2 = input("Enter the second word: ")
  
  if len(word1) == len(word2):
    list_w1 = word_to_list(word1)
    list_w2 = word_to_list(word2)

    for e in range(len(word1)):
      for i in range(len(word1)):
        if list_w1[e] != list_w2[i]:
          print("The words aren't anagram. ")
          return

  print("The words are anagram. ")
  


#___________________________________

def options(opt):

    match opt:
     case 1:
       calculator()
     case 2: 
       multiplication_table()
     case 3: 
       num = int(input("Enter the number: "))
       sum_of_firstn_numbers(num)
     case 4:
       guess_the_number()
     case 5:
       palindrome_checker()
     case 6: 
       list_filter()
     case 7:
       word_counter()
     case 8:
       max_min_average()
     case 9:
       fibonacci_sequence()
     case 10: 
       anagram_checker()
     case _:
       print("optn")


def main():
    print("Main\n")
    
    print("1. Calculator")
    print("2. Multiplication table")
    print("3. Sum of first N numbers")
    print("4. Guess the number")
    print("5. Palindrome checker")
    print("6. List filter")
    print("7. Word counter ")
    print("8. Max, min and average")
    print("9. Finonacci sequence")
    print("10. Anagram checker")
    print("11. Rock, paper, scissors game")
    print("12. Unique characters")
    print("13. Frequency counter")
    print("14. Simple login system")
    opt = int(input("\nEnter the option: "))
    options(opt)


main()



