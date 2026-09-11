# Phase 0 · Topic 1: Linear Algebra · Lesson 1: Vectors

Status: learning; quiz answers and learner execution pending. This is the first named subtopic on PDF page 2. No topic has been completed yet.

## Starting from your answer

You said: "we need to represent the number and direction to make the meaning of this question".

That is correct for movement. The missing detail is how to record both parts without ambiguity. Choose a convention: the first component describes east/west movement, the second north/south movement. Positive means east or north; negative means west or south. The movement in the question is then **(3, 2)**.

## A. What a vector is and why it matters

In the numerical form we will use, a vector is an ordered collection of numbers, called components, treated as one object. You can add vectors and multiply them by a single number.

A movement vector can describe a change in position. In machine learning, a vector often describes several measurements for one example. A house might be represented by (90, 3, 2), with components meaning floor area in square metres, bedrooms, and bathrooms. Those components are measurements, not compass directions. Their meanings and order must be recorded.

A **scalar** is one number, such as a temperature of 25 degrees. A vector can carry several components together. Its **dimension** is the number of components: (3, 2) is two-dimensional; the house example is three-dimensional. Numerical vectors can have many more than three components.

## B. Intuition: one arrow summarizing a movement

Imagine standing on a square grid. Walk 3 steps east, then 2 north. Draw an arrow from your starting point to your finishing point. The vector (3, 2) describes that overall change in position, called displacement.

The arrow is a useful picture because its length and pointing direction summarize the displacement. You can start that same movement at another location: the start and end positions change, but the displacement remains (3, 2).

The vector does not record the full route or the order in which you walked. You walked 5 steps along the two grid segments; the straight-line displacement is shorter. Also, (3, 2) and (2, 3) are different vectors because order matters.

## C. Mathematics needed for this lesson

Use the same coordinate convention and compatible units when combining movement vectors. For v = (v_x, v_y), the subscripts x and y just name its two components.

### Components and signs

- (3, 2): 3 east, 2 north.
- (-3, 2): 3 west, 2 north.
- (0, 0): no net displacement. The zero vector has length zero and no direction.

### Adding and subtracting vectors

Add matching components to combine movements:

`(v_x, v_y) + (w_x, w_y) = (v_x + w_x, v_y + w_y)`

For v = (3, 2) and w = (2, -1):

`v + w = (3 + 2, 2 - 1) = (5, 1)`

Subtract matching components in the same way:

`v - w = (3 - 2, 2 - (-1)) = (1, 3)`

Vectors must have the same number of components for these operations. In an application, matching positions must also refer to the same kind of measurement.

### Multiplying by a scalar

Multiply every component by the same number:

`k v = (k v_x, k v_y)`

For v = (3, 2): 2v = (6, 4), -v = (-3, -2), and 0v = (0, 0). A positive multiplier keeps the direction, a negative one reverses it, and the length is multiplied by the absolute value of k. Zero gives the zero vector, which has no direction.

### Length: the Euclidean norm

For perpendicular x and y axes measured in the same units, the components form the two short sides of a right triangle. Pythagoras gives:

`length(v) = sqrt(v_x^2 + v_y^2)`

For (3, 2), the length is sqrt(9 + 4) = sqrt(13), approximately **3.606 steps**. It is not 3 + 2. The original east-then-north route is 5 steps long; the norm measures straight-line displacement.

For more components, square each component, add the squares, then take the square root. Raw distances between mixed-unit feature vectors, such as area and bedroom count, need care; we will study feature scaling in its proper roadmap context.

### Unit vectors: keeping direction with length one

For a nonzero vector, divide every component by its length:

`unit(v) = (v_x / length(v), v_y / length(v))`

For (3, 2), this is approximately (0.832, 0.555). Its length is 1, apart from rounding. It points in the same direction as the original vector. You cannot apply this rule to (0, 0): it would divide by zero, and zero has no direction to preserve.

### Dot product: multiply matching components, then add

`v dot w = v_x * w_x + v_y * w_y`

For v = (3, 2) and w = (2, -1), the dot product is 3*2 + 2*(-1) = **4**. The result is a scalar, not another vector.

For nonzero movement vectors in the same ordinary coordinate system, a positive dot product means the angle between them is less than 90 degrees, zero means perpendicular, and a negative result means more than 90 degrees. Positive does not necessarily mean exactly the same direction. If either vector is zero, the dot product is also zero, but a geometric direction or angle for that vector is undefined.

We will reuse these operations later when comparing numerical representations and building models. Matrices and other later topics remain locked.

## D. Runnable example

Open `example.py` in this folder. It uses only basic variables, arithmetic, printing, and a condition for the zero-vector case. No NumPy, lists, or other packages are needed.

From your repository root, run:

```bash
python3 phase-00-foundations/01-linear-algebra/01-vectors/example.py
```

`** 0.5` computes a square root. `** 2` squares a number. `round(value, 3)` displays a number rounded to three decimal places.

The mentor executed this teaching example; its actual output is in `evidence/example-output.txt`. Your own run is still pending. Read the output and connect each number to the calculation above. Before editing the example, predict what will change if v_x becomes negative, then run it to compare your prediction.

## E. Quiz: answer before receiving solutions

Answer the five questions in `quiz.md`, showing your reasoning. Do not just copy values from a calculator. The quiz has not been answered or passed.

## F. Mini-project: next, after quiz review

After the answers are reviewed and any gaps corrected, the mentor will assign the learner-built vector project with a precise input/output contract and acceptance criteria. The scope remains 1–3 study days at two hours per day. The teaching example is not the learner's project.

The final checkpoint will require the learner to confirm understanding, completion of the reviewed quiz, and completion and GitHub publication of the project. None of those checks has passed yet.
