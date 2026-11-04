# Python Conditional Statements — Smart Canteen Discount System

A beginner-friendly Python console program created during the Python lecture on **conditional statements**. It demonstrates how a program makes decisions using `if`, `elif`, and `else` in a realistic college-canteen scenario.

## Repository Name

`python-conditionals-smart-canteen`

## Class Demonstration

The class used a canteen bill to explain how conditions choose one outcome from several possible outcomes.

| Bill Amount | Standard Discount |
|---|---:|
| Rs. 3,000 or more | 20% |
| Rs. 2,000 to below Rs. 3,000 | 10% |
| Rs. 1,000 to below Rs. 2,000 | 5% |
| Below Rs. 1,000 | 0% |

The program displays the original bill, membership status, total discount rate, discount amount, and final payable amount.

## Concepts Covered

- `if`: runs a block when a condition is true.
- `elif`: checks another condition when earlier conditions were false.
- `else`: handles the remaining case when no previous condition matched.
- Comparison operators such as `>=`, `<=`, and `>`.
- Input using `input()` and numeric conversion using `float()`.
- String methods: `strip()` and `lower()` for normalizing the membership response.
- Conditional logic for membership-based discounts.
- Calculations with percentages.
- String formatting using f-strings and `:.2f`.
- Nested conditional logic and sequential decision-making.

## Program Logic and Enhancements

The lecture's student challenges are reflected in the current code:

1. **Bill validation:** Rejects bill amounts that are zero or negative.
2. **Membership prompt:** Asks whether the student has a membership card.
3. **Membership discount:** Adds 5 percentage points to the standard discount rate when the entered response is `yes`.
4. **Savings message:** Displays a congratulatory message when the calculated discount is greater than zero.
5. **Bill summary:** Displays the membership response, total discount rate, discount amount, and final payable amount.

### Important Discount Calculation

The membership benefit is added to the **standard discount rate**, and the resulting combined rate is calculated against the original bill amount. It is not calculated on the remaining balance after the standard discount.

For example, for a bill of Rs. 3,000:

- Standard discount rate: 20%
- Additional membership benefit: 5 percentage points
- Total discount rate: 25%
- Total discount: Rs. 3,000 × 25% = Rs. 750
- Final payable amount: Rs. 3,000 − Rs. 750 = Rs. 2,250

**Input-validation note:** The current program checks whether the numeric bill amount is greater than zero. It does not yet handle non-numeric bill input with `try/except`, and it does not reject membership responses other than `yes` or `no`. Only an exact `yes` response (after trimming surrounding spaces and converting to lowercase) activates the membership benefit.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python smart_canteen_discount.py
```

On some systems, use `python3` instead of `python`.

## Example Run

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 3000
Do you have a membership card? (yes/no): yes

===== BILL SUMMARY =====
Original Bill: Rs. 3000.00
Membership Card: Yes
Total Discount Rate: 25%
Discount Amount: Rs. 750.00
Final Payable: Rs. 2250.00
Congratulations! You saved Rs. 750.00
```

## UI/UX Notes

This is a **console-based** program, not a graphical web interface. Its basic user-experience choices are:

- A clear title and bill-summary heading.
- Direct prompts that tell the user what to enter.
- Currency labels (`Rs.`) and two decimal places for monetary amounts.
- A readable summary showing the membership response and discount calculation.
- An error message when the bill amount is zero or negative.
- A congratulatory message when a discount is applied.

These choices make the output easier for a beginner to follow. A future extension could add stronger input validation, a graphical interface, or a web page, but those features are outside the scope of the current Python conditionals exercise.

## Practice Challenges

1. Add a rule that rejects membership answers other than `yes` or `no`.
2. Add `try/except` handling for non-numeric bill input.
3. Add a student category (e.g., regular student or staff) and introduce a new condition.
4. Add a maximum discount limit.
5. Print which standard discount tier was selected.
6. Explain why `elif` is suitable here instead of several independent `if` statements.

## Suggested Git Commit

```text
Update README to match smart canteen discount logic
```

## Suggested Repository Description

Beginner Python lesson demonstrating if, elif, else, comparison operators, membership-based discount calculations, and basic bill validation in a real-world canteen discount calculator.
