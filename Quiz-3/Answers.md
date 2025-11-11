# Answers to the Quiz 3

## Q1

a) Admissible heuristic is a function that does not overestimate the cost of reaching a goal state from a current point. 

b) h=0 can be admissible function as the cost of reaching the goal can be 0 i.e. you are already present at the goal state.

c) h=k for a given problem is admissible if and only if k is a value that is lower than the true cost k*.

d) h = min (h1,h2,h3) will be admissible as it will be the lowest value of the range, and regardless of the true cost of the function, the minimum value will always be less. On the other hand h = max(h1.h2,h3) will not be admissible as we cannot guarantee if the maximum value of the range is the actual cost of the function. 


## Q2

1) The code provided implements representation that shows how many cannibals and missionaries are moved in each move. The first number is the number of missionaries (M) and the second is the number of cannibals(C). First it shows boat going from right to left, how many of each M or C it holds. then it shows the boat coming back from left to right, with however many of each passengers. It continues to show this back and forth movement of the boat from bank to bank. It uses a breadth first search strategy. A queue allows us to use a first in first out strategy, so that we can go through the breadth of the search tree

2) Done in code
I decided to use a depth first search. Since stack data structure already holds the last in first out idea, it is the easiest to use a stack to 


3) Done in code

## Q3

a) The cryptic problem: T W O + T W O = F O U R

Variables are: F, O, R, T, U, W, X1, X2, X3
Domain is: {0,1,2,3,4,5,6,7,8,9}
Constraints are: alldiff(F, O, R, T, U, W), T does not equal 0 (unary constraint), O+O = R + 10 * X1, W+W = U + 10*X2, T+T = F + 10*X3, T does not equal F, w, O, U, R. F does not equal T, w, O, U, R. W does not equal F, T, O, U, R. O does not equal F, w, T, U, R. U does not equal F, w, O, T, R. R does not equal F, w, O, U, T.

b) we can use the arc constistency path discussed in class, because of the binary constraint nature of the problem.
pseudocode:


