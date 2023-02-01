# CMPS 2200  Recitation 01

**Name (Team Member 1):**Ritika
**Name (Team Member 2):**Izzy

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment. 
- Click on your personal github repository for the assignment.
- Login in Repls https://replit.com/repls and then create a new replit by importing from github repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.
- Make sure the dependencies are installed. Please use 'pip install -r requirements.txt'.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 


- **The worst case input value key for linear search is when the key is not present in the list or the value is the last element of the list as in a linear search we go through the first element, the second element, all the way to the last element. The time complexity of O(n) illustrates how in a linear search the search goes through all n elements.
- The worse case input value of key for binary search is also when the key is not in the list or in the last position of the list. The search will first check if the key is in the middle and if its not it will determine if it is in the top half of the list starting from the middle or the bottom half of the list starting at the first element. It will keep eliminating half the elements in the list, and if the key is in the last element, it will go through the most illeterations. Binary search's time complexity is still faster than linear search's time complexity as O(logn) is faster than O(n).**
- 
- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`?
       

**The best case input value of key for linear search would be when the key is the first element in the list as linear search starts searching for values starting with the first element in the list. If the key is in the first element of the list, the search will return the position of the key and won't have to go through the rest of the elements. The best case input value of key for the binary search algorithm is when the key is located in the middle of the list. The binary search algorithm will perform log2(n) iterations as it will won't have to keep halving the list as it will immediately find the key in the middle. **

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.


- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.


- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**0.09274482727050781
0.014543533325195312
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.003 |    0.004 |
|      100 |    0.010 |    0.004 |
|     1000 |    0.097 |    0.007 |
|    10000 |    0.950 |    0.011 |
|   100000 |    9.414 |    0.020 |
|  1000000 |  195.478 |    0.022 |
| 10000000 | 2030.011 |    0.188 |**

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**The theoritical runtime does not match the linear search runtime as I plotted n and the results from the linear search and the relationship is not linear and this could be because of many things such as the performance of my algorithm or my macbook. The theoritical results do match the running times of the binary search pretty well after I plotted them.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: The worst time case complexity of searching n elements using a list of n elements with linear search is 0(nk).**
  + For binary search? **TODO: The worst time case complexity for searching a list using binary search is O(n log n + k log n)**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: For the values of k it is more efficient to sort the list and then use binary search is if K is larger than n^2/log n**
