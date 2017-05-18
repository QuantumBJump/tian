# tian
a dice parsing package by Quinn Stevens

## Index

* [Change log](#change-log)
* [Usage](#usage)
* [Notation](#notation)

### Change log

#### 0.1
* Created package
* Added [x]d[y] functionality
* Added arithmetic functionality
* Added k[x]h/l functionality
* Added rr[x] functionality

### Usage

To use tian, simply install it using `pip install tian`, and then use the `roll()` command, passing as a string the roll you want to make, and the function will return the result of the roll as an integer.

### Notation

tian uses dice notation similar to that used by the [roll20](https://roll20.net) engine, although as of yet it doesn't support the full range of functionality in that engine. The currently supported functionality is listed below:

* **[x]d[y]:** This will roll x y-sided dice and returns the sum - for instance, `roll("5d6")` will roll 5 six-sided dice
* **arithmetic:** tian currently supports all four basic arithmetic operations, +, -, * and /. So `roll("1d8 + 4")` will roll an eight-sided die and add 4 to the result
* **k[x]h/k[x]l:** put after a roll, this will keep the x highest or lowest results rolled - `roll("4d6 k3h")` rolls 4 six-sided dice and keeps the 3 highest (or discards the lowest) rolls, so a result of 4, 5, 2, 6 would resolve as 4+5+6 = 15
* **rr[x]:** put after a roll, this will reroll results equal to or lower than x, but *only once* - if you reroll a 1 and get another 1, you're stuck with it
