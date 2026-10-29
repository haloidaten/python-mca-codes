[README.md](https://github.com/user-attachments/files/34118368/README.md)
# Python Programming Practicals

## About This Repository
This repository contains 26 Python programs for practising fundamental programming concepts, including mathematical calculations, conditional statements, loops, strings, lists, dictionaries, list comprehensions, lambda functions, and pattern printing.

## Requirements
- Python 3.x
- A Python editor or IDE, such as IDLE, VS Code, or PyCharm

## How to Run a Program
1. Install Python 3.
2. Open a terminal or command prompt in the folder containing the programs.
3. Run a program using the command below, replacing the filename with the program you want to execute:

   ```bash
   python prg1.py
   ```

   On some systems, you may need to use `python3` instead of `python`.

---

## Program 1: Display Leap Years
**File:** `prg1.py`

**Description:** Displays leap years from the current year through the year entered by the user.

**Concepts:** `datetime` module, `for` loop, conditions, leap-year rules.

**Example:** If the current year is 2026 and the user enters `2030`, the program displays `2028`.

**Learning outcome:** Identify leap years using divisibility rules.

---

## Program 2: Replace Repeated First Characters
**File:** `prg2.py`

**Description:** Keeps the first character of a string and replaces later occurrences of that character with `$`.

**Concepts:** String indexing, slicing, `replace()`.

**Example:** Input `abacus` produces `ab$cus`.

**Learning outcome:** Practise string manipulation.

---

## Program 3: Swap the First and Last Characters
**File:** `prg3.py`

**Description:** Swaps the first and last characters of a string while keeping the middle characters unchanged.

**Concepts:** String indexing, slicing, `if` statement.

**Example:** Input `Python` produces `nythoP`.

**Learning outcome:** Understand string positions and slicing.

---

## Program 4: Calculate the Area of a Circle
**File:** `prg4.py`

**Description:** Calculates the area of a circle using the radius entered by the user.

**Formula:** Area = π × radius²

**Concepts:** `math` module, `math.pi`, floating-point input, arithmetic.

**Example:** Radius `5` produces an area of approximately `78.54`.

**Learning outcome:** Apply a mathematical formula in Python.

---

## Program 5: Find the Largest of Three Numbers
**File:** `prg5.py`

**Description:** Reads three numbers and displays the largest one.

**Concepts:** `if`, `elif`, `else`, comparison operators, numeric input.

**Example:** Inputs `10`, `25`, and `15` produce `25.0`.

**Learning outcome:** Compare values using conditional statements.

---

## Program 6: Find a File Extension
**File:** `prg6.py`

**Description:** Splits a filename at periods and displays the final part as the extension.

**Concepts:** `input()`, `split()`, negative indexing.

**Example:** Input `document.pdf` produces `pdf`.

**Learning outcome:** Extract information from a string.

---

## Program 7: Calculate a Repeated-Number Sum
**File:** `prg7.py`

**Description:** Adds a number to the number formed by repeating its digits twice and the number formed by repeating its digits three times.

**Concepts:** String conversion, string repetition, `int()`, arithmetic.

**Example:** Input `5` calculates `5 + 55 + 555` and produces `615`.

**Learning outcome:** Combine string operations and arithmetic.

---

## Program 8: List Comprehension Exercises
**File:** `prg8.py`

This file contains four exercises:

1. **Positive numbers:** Selects positive values from a predefined list.
2. **Squares:** Reads numbers and creates a list of their squares.
3. **Vowels:** Extracts vowels from a word.
4. **Ordinal values:** Uses `ord()` to obtain the Unicode code point of each character.

**Concepts:** Lists, list comprehensions, conditions, `ord()`.

**Example:** The vowel exercise with `Education` produces `['E', 'u', 'a', 'i', 'o']`.

**Learning outcome:** Use concise list comprehensions to process data.

---

## Program 9: Count Word Occurrences
**File:** `prg9.py`

**Description:** Counts how many times each word appears in a line of text and displays the counts.

**Concepts:** `split()`, dictionaries, `for` loops, `dict.get()`.

**Example:** Input `Python is easy and Python is useful` counts `Python` twice and `is` twice.

**Learning outcome:** Count repeated items using a dictionary.

**Note:** Words are counted exactly as entered, so capitalisation and punctuation may affect the count.

---

## Program 10: Replace Numbers Greater Than 100
**File:** `prg10.py`

**Description:** Reads integers separated by spaces and replaces values greater than `100` with the string `over`.

**Concepts:** `map()`, lists, list comprehension, conditional expression.

**Example:** Input `10 150 80 200 50` produces `[10, 'over', 80, 'over', 50]`.

**Learning outcome:** Filter or transform list values according to a condition.

---

## Program 11: Count the Letter 'a' in Names
**File:** `prg11.py`

**Description:** Reads names separated by spaces and counts all occurrences of the letter `a`, without distinguishing uppercase and lowercase.

**Concepts:** `split()`, `lower()`, `count()`, `sum()`.

**Example:** Input `Rahul Aman Arav` produces `5`.

**Learning outcome:** Count a character across multiple strings.

---

## Program 12: Compare Two Lists
**File:** `prg12.py`

**Description:** Reads two lists of integers and checks whether they have the same length, the same sum, and at least one common value.

**Concepts:** Lists, `len()`, `sum()`, `any()`, membership tests, conditions.

**Learning outcome:** Compare lists using their length, total, and elements.

---

## Program 13: Display the First and Last Colours
**File:** `prg13.py`

**Description:** Reads comma-separated colour names and displays the first and last entries.

**Concepts:** `split()`, lists, indexing.

**Example:** Input `red,green,blue,yellow` displays `red` and `yellow`.

**Learning outcome:** Access list elements by index.

---

## Program 14: Find Colours Present Only in the First List
**File:** `prg14.py`

**Description:** Reads two comma-separated colour lists and displays colours that occur in the first list but not in the second.

**Concepts:** Lists, list comprehension, membership operator `not in`.

**Example:** Lists `red,green,blue` and `green,yellow` produce `['red', 'blue']`.

**Learning outcome:** Filter list elements based on membership in another list.

---

## Program 15: Remove Even Numbers
**File:** `prg15.py`

**Description:** Reads integers and creates a list containing only odd numbers, thereby removing even numbers.

**Concepts:** Lists, `map()`, list comprehension, modulus operator `%`.

**Example:** Input `1 2 3 4 5 6` produces `[1, 3, 5]`.

**Learning outcome:** Select numbers based on whether they are odd or even.

---

## Program 16: Calculate a Factorial
**File:** `prg16.py`

**Description:** Calculates the factorial of an entered number by multiplying the integers from `1` through that number.

**Formula:** `n! = n × (n - 1) × ... × 1`

**Example:** Input `5` produces `120`.

**Concepts:** `for` loop, accumulator variable, multiplication, `range()`.

**Learning outcome:** Use a loop to calculate a product.

**Note:** The program is intended for non-negative integers. It does not validate negative input.

---

## Program 17: Generate the Fibonacci Series
**File:** `prg17.py`

**Description:** Displays the requested number of terms in the Fibonacci series. Each term after the first two is the sum of the previous two terms.

**Example:** For `7` terms, the output is `0 1 1 2 3 5 8`.

**Concepts:** Loops, variable updates, arithmetic.

**Learning outcome:** Generate a sequence using repeated variable updates.

---

## Program 18: Calculate a Running Sum
**File:** `prg18.py`

**Description:** Adds each number in a predefined list to a running total and prints the total after every addition.

**Example:** For `[10, 20, 30, 40, 50]`, the running totals are `10`, `30`, `60`, `100`, and `150`.

**Concepts:** Lists, `for` loops, accumulator variables.

**Learning outcome:** Understand cumulative totals.

---

## Program 19: Find Four-Digit Perfect Squares with Even Digits
**File:** `prg19.py`

**Description:** Searches a user-specified range for four-digit numbers whose digits are all even and which are perfect squares.

**Concepts:** Loops, string conversion, `all()`, digit checking, square-root calculation.

**Example:** `4624` satisfies the conditions because every digit is even and `4624 = 68²`.

**Learning outcome:** Combine digit checks with a mathematical condition to find numbers.

---

## Program 20: Count Character Frequencies
**File:** `prg20.py`

**Description:** Counts the number of occurrences of each character in an entered string using a dictionary.

**Example:** For `banana`, the final frequency dictionary is `{'b': 1, 'a': 3, 'n': 2}`.

**Concepts:** Strings, dictionaries, loops, conditions.

**Learning outcome:** Store and update character frequencies.

**Note:** The current program prints the dictionary during each loop iteration, so intermediate dictionaries appear before the final result.

---

## Program 21: Add 'ing' or 'ly' to a String
**File:** `prg21.py`

**Description:** If the entered string ends with `ing`, appends `ly`. Otherwise, appends `ing`.

**Concepts:** Strings, `endswith()`, conditional statements, concatenation.

**Examples:**
- Input `play` produces `playing`.
- Input `playing` produces `playingly`.

**Learning outcome:** Modify strings based on their endings.

---

## Program 22: Find the Longest Word
**File:** `prg22.py`

**Description:** Reads words separated by spaces and displays the longest word and its length.

**Concepts:** `split()`, `max()`, `len()`, the `key` argument.

**Example:** Input `Python is powerful` displays `powerful` and its length, `8`.

**Learning outcome:** Find the longest item in a collection using a built-in function.

**Note:** The program expects at least one word.

---

## Program 23: Print a Multiplication Pattern
**File:** `prg23.py`

**Description:** Reads the number of steps and prints a triangular pattern in which each row contains multiples of its row number.

**Example:** For `n = 4`:

```text
1
2 4
3 6 9
4 8 12 16
```

**Concepts:** Nested `for` loops, `range()`, multiplication, `print(end=" ")`.

**Learning outcome:** Use nested loops to create number patterns.

---

## Program 24: Print a Star Diamond Pattern
**File:** `prg24.py`

**Description:** Prints an increasing and then decreasing star pattern using a fixed value of `n = 5`.

**Example output:**

```text
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

**Concepts:** Nested loops, `range()`, iteration, pattern printing.

**Learning outcome:** Understand how nested loops control rows and columns in a pattern.

---

## Program 25: Find the Factors of a Number
**File:** `prg25.py`

**Description:** Reads a number and displays all integers from `1` through that number that divide it exactly.

**Example:** Input `12` produces the factors `1`, `2`, `3`, `4`, `6`, and `12`.

**Concepts:** `for` loops, modulus operator `%`, conditional statements.

**Learning outcome:** Find factors by checking whether the remainder is zero.

**Note:** The program is intended for positive integers.

---

## Program 26: Calculate Areas Using Lambda Functions
**File:** `prg26.py`

**Description:** Uses lambda functions to calculate the areas of a square, rectangle, and triangle.

**Formulas:**
- Square: `side × side`
- Rectangle: `length × breadth`
- Triangle: `0.5 × base × height`

**Concepts:** Lambda functions, variables, user input, floating-point arithmetic.

**Learning outcome:** Define short anonymous functions and use them for mathematical calculations.

---

Practising these programs helps build a foundation for more advanced programming and problem-solving.
