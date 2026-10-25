
# Campus Canteen Pre-Order System - CI Pipeline

## Objective
Implement and test the calculate_total() function
using Python and GitHub Actions.

## Business Rules
- GST: 5%
- Discount: 10% for subtotals above Rs. 300
- GST is calculated after the discount.
- Final amounts are rounded to two decimal places.

## Technologies
- Python 3.12
- pytest
- Git and GitHub
- GitHub Actions

## Setup
Install dependencies:

    python -m pip install -r requirements.txt

Run tests:

    python -m pytest -v

## CI Pipeline
The workflow runs automated tests on every push
and pull request.

## Test Coverage
- Normal order
- Discount threshold
- Discounted order
- Subtotal just above the threshold
- Zero-value order
- Negative subtotal validation
