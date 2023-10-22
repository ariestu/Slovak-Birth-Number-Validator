# birthNumberValidator
python scripts verifies whether a slovak birth number (rodne cislo) is valid and returns information fetched from the birth number

script handles both birth numbers with or without slash\
scrips handles 9 digit birth numbers assigned before 1954 and changes the final message accordingly\
script checks for valid format, lenght, day, month and control digit\
\
the maximum allowed age is 100 (101 if the birthday already happened in the current year), when an older birth number is enter script returns error; the maximum age can be change in a variable
  HOWEVER the logic can only handle birth numbers from 20th and 21st century
