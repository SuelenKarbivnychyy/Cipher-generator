"""This program encode and decode a message based on user's input."""

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  
def caesar(start_text, shift_amount, cipher_direction): 
  
  end_text = ""  
  
  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:  
      position = alphabet.index(char)
      new_index_position = position + shift_amount
      new_position = new_index_position % len(alphabet)    
      end_text += alphabet[new_position]
    
  print(f"\nHere's the {cipher_direction}d result: {end_text}")

  
reestart_program = True
while reestart_program:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))
  
 
  #the program continues to work even if the user enters a shift number greater than 26.
  #pseudocode:
  #get the index of letter
  #create a new_index variable and add the shift plus the letter's index
  #get the remainder of new_index % len(alphabet)
  #that remainder is going to be the index of new letter

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  wants_new_message = input("\nDo you want to reestart the program? Type 'yes' or 'no': \n").lower()
  
  if wants_new_message == "yes":
    reestart_program
  else:
    reestart_program = False
    print("Goodbye")