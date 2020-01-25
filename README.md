# Sinabs

### What is Sinabs?

Sinabs stands for "Sinabs is not a bill splitter".
The purpose behind it is to be a simple, but handy tool, which helps users to figure out,
how to properly split payments between them.

### How to use Sinabs?

Using Sinabs is very easy.
It is best explained with a simple example:

Alice, Bob and Charlie went on a trip together.
Alice paid the gas bill, which was 35.13$.
Bob paid for Dinner for all of them, which was 60$.
He also paid for breakfast, which was 17.68$
Charlie paid for the accommodation, which was 73$.
Charlie also got a tax return for the accommodation of 6.34$.
Now they want to use Sinabs to split the bill equally.
Here is how they go about:

 - They start Sinabs by running `python src/sinabs.py`, upon which they get greeted by  
 `Welcome to Sinabs!`  
  `How many people want to split the bill?`
 - Since they are three people, they type `3` and press enter. Now they get prompted by  
 `Please enter the name of person 1.`
 - Let's say Alice is going ot be person 1, so they type `Alice` and press enter again.
 The next prompt that shows up is  
 `Please enter Alice's first spending (0 to quit).`
 - Now they enter the 35.13 that Alice spent on the gas bill
 (Make sure to omit the $-sign). The next prompt asks for her next payment.
 - Since Alice had only one spending, they now enter a `0`, which triggers the next prompt,
 asking for the name of person 2. 
 - They proceed in the same way as before, by entering `Bob` and pressing enter.
 - When they are prompted for Bob's first payment, they enter `60`. 
 - When they are prompted for his next payment, they do not enter `0`, but `17.68`.
 - Since that was Bob's last payment, they now enter a `0`.
 - Now they do the same for Charlie's name and first payment.
 - Since Charlie's second payment is a return, it has to be entered as a negative number,
 i.e. `-6.34`.
 - After they now enter a `0` to indicate, that no more payments were done, Sinabs
 calculates they best way to split their bill.
 
The entire process looks like the following:

```
Welcome to Sinabs!  
How many people want to split the bill?  
3  
Please enter the name of person 1.  
Alice  
Please enter Alice's first spending (0 to quit).  
35.13  
Please enter Alice's next spending.  
0  
Please enter the name of person 2.  
Bob   
Please enter Bob's first spending (0 to quit).  
60  
Please enter Bob's next spending.  
17.68  
Please enter Bob's next spending.  
0  
Please enter the name of person 3.  
Charlie  
Please enter Charlie's first spending (0 to quit).  
73  
Please enter Charlie's next spending.  
-6.34  
Please enter Charlie's next spending.  
0  
The initial balance after all spendings are:  
Alice: 35.13  
Bob: 77.68  
Charlie: 66.66  
Alice has to pay 17.86 to Bob  
Alice has to pay 6.84 to Charlie  
```
The output tells them two things:
  - The amount of money spent by each person
  - The transactions they need to do, in order to balance them.
  
They see, that Alice spent the least amount of money, so she has to pay 17.86$ to Bob and
6.84$ to Charlie.
After this is done, everyone spent a total of 59.82$ for the trip.

So, if you want to use Sinabs to split your own bills, just do it like Alice, Bob and Charlie:
- Enter, how many people you are
- Enter your names
- Enter your spendings

Afterwards, Sinabs calculates the best way to split the bill equally.
Now you can use cash or your preferred form of digital payment to even out your payments in a fair way!