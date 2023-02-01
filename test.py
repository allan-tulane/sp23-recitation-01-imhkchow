"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
  """ done. """
  for i, v in enumerate(mylist):
    if v == key:
      return i
  return -1


print(linear_search([1, 2, 3, 4, 5], 5))


def test_linear_search():
  """ done. """
  assert linear_search([1, 2, 3, 4, 5], 5) == 4
  assert linear_search([1, 2, 3, 4, 5], 1) == 0
  assert linear_search([1, 2, 3, 4, 5], 6) == -1


def binary_search(mylist, key):
  return _binary_search(mylist, key, 0, len(mylist) - 1)
  """
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
# 	"""


def _binary_search(mylist, key, left, right):
  if left > right:
    return -1
  mid = (left + right) // 2
  if mylist[mid] == key:
    return mid
  elif mylist[mid] > key:
    return _binary_search(mylist, key, left, mid - 1)
  else:
    return _binary_search(mylist, key, mid + 1, right)


def test_binary_search():
  assert binary_search([1, 2, 3, 4, 5], 5) == 4
  assert binary_search([1, 2, 3, 4, 5], 1) == 0
  assert binary_search([1, 2, 3, 4, 5], 6) == -1


def time_search(sort_fn, mylist, key):
  beginning = time.perf_counter()
  sort_fn(mylist, key)
  endfunction = time.perf_counter()
  return (endfunction - beginning) * 1000


##
#what is the difference between search_fn and sort_fn if we are passing them both into the function.


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  results = []
  for n in sizes:
    linear_time = time_search(linear_search, sizes, -1)
    binary_time = time_search(binary_search, sizes, -1)
    results.append((n, linear_time, binary_time))
  return results


###


def print_results(results):
  """ done """
  print(
    tabulate.tabulate(results,
                      headers=['n', 'linear', 'binary'],
                      floatfmt=".3f",
                      tablefmt="github"))


print_results(compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]))


def test_compare_search():
  res = compare_search(sizes=[10, 100])
  print(res)
  assert res[0][0] == 10
  assert res[1][0] == 100
  assert res[0][1] < 1
  assert res[1][1] < 1
