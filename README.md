# Lab Assignment #2 – Algorithm Analysis

Purpose: The purpose of this Lab assignment is to:

- Perform experimental analysis of algorithms

- Explain and proof the running time of algorithms in terms of big-Oh
    notation

- Design various algorithm that achieve a specified running time

References: Read the course’s text chapter 4 and the lecture slides.
This material provides the necessary information that you need to
complete the exercises.

## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

1. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example1** method from **Exercises.java** class in
    Lesson 4 examples.

2. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example2** method from **Exercises.java** class in
    Lesson 4 examples.

3. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example3** method from **Exercises.java** class in
    Lesson 4 examples.

4. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example4** method from **Exercises.java** class in
    Lesson 4 examples.

5. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example5** method from **Exercises.java** class in
    Lesson 4 examples.

For each of the above questions, use comments in the code to provide the
results and a brief explanation.

**If your first name starts with a letter from K-Z inclusively:**

1. . Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example1** method from **Exercises2.java** class in
    Lesson 4 examples.

2. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example2** method from **Exercises2.java** class in
    Lesson 4 examples.

3. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example3** method from **Exercises.2java** class in
    Lesson 4 examples.

4. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example4** method from **Exercises2.java** class in
    Lesson 4 examples.

5. Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example5** method from **Exercises2.java** class in
    Lesson 4 examples.

(3 marks)

## Exercise 2

**If your first name starts with a letter from A-J inclusively:**

Perform an **experimental analysis** of the two algorithms
*prefixAverage1* and *prefixAverage2*, from lesson examples. Optionally,
visualize their running times as **a function of the input size** with a
**log-log chart**. Use either Java or Python graphical capabilities for
visualization.

**Hint**: Choose representative values of the input size **n**, similar
to *StringExperiment.java* from class examples.

**If your first name starts with a letter from K-Z inclusively:**

For each of the algorithms *unique1* and *unique2* (*Uniqueness.java*
class in Lesson 4 examples) which solve the element uniqueness problem,
perform an experimental analysis to determine the largest value of
***n*** such that the given algorithm runs in one minute or less.

**Hint**: Do a type of “binary search” to determine the maximum
effective value of ***n*** for each algorithm.

> (4 marks)

## Exercise 3

**If your first name starts with a letter from A-J inclusively:**

An array A contains n−1 unique integers in the range \[0,n−1\], that is,
there is one number from this range that is not in A. Design an
O(n)-time algorithm for finding that number. You are only allowed to use
O(1) additional space besides the array A itself. Write the java method
that implements this algorithm and a main method to test it.

**Hint:** Numbers in \[0, n-1\] form an arithmetic progression whose sum
is known.

**If your first name starts with a letter from K-Z inclusively:**

Given an array A of n arbitrary integers, design an O(n)-time algorithm
for finding an integer that cannot be formed as the sum of two integers
in A. Write the java method that implements this algorithm and a main
method to test it.

**Hint** The sum of every two integers in A is always less or equal to
twice the maximum element.

> (3 marks)

**Evaluation:**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Functionality</strong></p>
<ul>
<li><p>Correct result of running time</p></li>
<li><p>Correct experimental analyses code and visualization</p></li>
<li><p>Code demonstration and brief explanation of proof or analyses in
a short video</p></li>
</ul></th>
<th><p>20%</p>
<p>40%</p>
<p>10%</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Object Oriented Design</strong></p>
<ul>
<li><p>Correct design of classes and methods similarly to chapter 3
examples.</p></li>
<li><p>Correct use of generics</p></li>
<li><p>Correct use of naming guidelines for classes, variables, methods,
packages.</p></li>
</ul></td>
<td><p>15%</p>
<p>5%</p></td>
</tr>
<tr class="even">
<td><strong>Friendly graphical display</strong></td>
<td>10%</td>
</tr>
<tr class="odd">
<td><strong>Total</strong></td>
<td>100%</td>
</tr>
</tbody>
</table>

**Naming and Submission Rules:**

You must **name your Eclipse project** according to the following rule:

**YourFullname_COMP254Labnumber**. Example: **JohnSmith_COMP254Lab2**

You must name package names
**com.exercisenumber.yourfirstname.yourlastname**, for example:
**com.exercise1.john.smith**

Provide your **student number and full name as a comment** at the top of
main method for each exercise.

**Archive your project in a zip file** named according to the following
rule:

**YourFullname_COMP254Labnumber.zip**

Example: **JohnSmith_COMP254Lab2.zip**

Upload the zip file on eCentennial using the Assignment link.

## Appendix

`exercises.py`
```python
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def example1(S):
  """Return the sum of the elements in sequence S."""
  n = len(S)
  total = 0
  for j in range(n):             # loop from 0 to n-1
    total += S[j]  # running time is O(n)
  return total

def example2(S):
  """Return the sum of the elements with even index in sequence S."""
  n = len(S)
  total = 0
  for j in range(0, n, 2):       # note the increment of 2
    total += S[j]
  return total
  
def example3(S):
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  total = 0
  for j in range(n):            # loop from 0 to n-1
    for k in range(1+j):        # loop from 0 to j
      total += S[k]
  return total

def example4(S):
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  prefix = 0
  total = 0
  for j in range(n):
    prefix += S[j]
    total += prefix
  return total

def example5(A, B):           # assume that A and B have equal length
  """Return the number of elements in B equal to the sum of prefix sums in A."""
  n = len(A)                  
  count = 0
  for i in range(n):          # loop from 0 to n-1
    total = 0
    for j in range(n):        # loop from 0 to n-1
      for k in range(1+j):    # loop from 0 to j
        total += A[k]
    if B[i] == total:
      count += 1
  return count
```

`prefix_averages.py`
```python
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def prefix_average1(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    total = 0                     # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)          # record the average
  return A

def prefix_average2(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    A[j] = sum(S[0:j+1]) / (j+1)  # record the average
  return A

def prefix_average3(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                   # create new list of n zeros
  total = 0                     # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j]               # update prefix sum to include S[j]
    A[j] = total / (j+1)        # compute average based on current sum
  return A
```

`unique.py`
```python
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False              # found duplicate pair
  return True                     # if we reach this, elements were unique

def unique2(S):
  """Return True if there are no duplicate elements in sequence S."""
  temp = sorted(S)                # create a sorted copy of S
  for j in range(1, len(temp)):
    if S[j-1] == S[j]:
      return False                # found duplicate pair
  return True                     # if we reach this, elements were unique
```
