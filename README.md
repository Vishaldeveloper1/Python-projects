# Python-projects
# How the Number guessing Game Works
To understand how the number guessing game functions, let’s walk through two practical scenarios. These examples demonstrate how narrowing down the range intelligently—similar to a binary search—can help guess the number efficiently.

Example 1: Guessing in a Range from 1 to 100
Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 50 → Too high
Guess 2: 25 → Too low
Guess 3: 37 → Too low
Guess 4: 43 → Too high
Guess 5: 40 → Too low
Guess 6: 41 → Too low
Guess 7: 42 → Correct!

Total Guesses: 7

Example 2: Guessing in a Range from 1 to 50
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 25 → Too low
Guess 2: 37 → Too low
Guess 3: 43 → Too high
Guess 4: 40 → Too low
Guess 5: 41 → Too low
Guess 6: 42 → Correct!

Total Guesses: 6

Note: In both examples, the user intelligently uses the binary search strategy, halving the guessing range with each attempt.

Algorithm:

Accept lower and upper bounds from the user.

Generate a random number in the selected range.

Calculate the maximum allowed guesses using the binary search formula.

Run a loop to take user guesses:
If the guess is too high, print: "Try Again! You guessed too high."
If the guess is too low, print: "Try Again! You guessed too small."
If the guess is correct, print: "Congratulations!" and exit the loop.
If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"

# Payment Recipt
Creating payment receipts is a pretty common task, be it an e-commerce website or any local store for that matter.

Here, we will see how to create our own transaction receipts just by using python. We would be using reportlab to generate the PDFs. Generally, it comes as a built-in package but sometimes it might not be present too. If it's not present, then simply type the following in your terminal

Installation:
pip install reportlab
Approach:
Import module.
We need the data in the form of a list of lists. The 0th index of the outer index is the headers.
We create a simple doc template with the specified paper size (here A4)
Then get a sample style sheet from the built-in style sheets and add the styling accordingly.
After you have created a style object, feed in the data and the style sheet to the pdf object and build it.
