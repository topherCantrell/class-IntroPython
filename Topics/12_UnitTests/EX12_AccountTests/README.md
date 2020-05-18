# Create a class for a checking account

The account has the following attributes:
  - name (required to create, read only after that)
  - phone (read/write, can be set on create)
  - balance (read-only,can be set on create)
  
The account has the following methods:
  - withdraw(amount) removes amount from balance
  - deposit(amount) adds amount to balance
  
Create accounts for Jack and Jill with $100 each. Write a function to
transfer money between two accounts. Take $25 from Jack and give it 
to Jill.