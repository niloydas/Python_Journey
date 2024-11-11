givenNumber=12345

while givenNumber > 0:

    digit = givenNumber % 10
  
    givenNumber = givenNumber // 10

    print(digit, end=" ")