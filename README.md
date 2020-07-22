# CS662Assignment1

 Due Date: Aug 31.

This assignment is meant to get you up to speed with Python, build a
couple of tools that we'll use later in the semester, and also give
you an early taste of machine learning using scikit-learn. For all
assignments, you must use the provided template code as a starting point.

(25%) Word frequencies. One of the primary domains we'll  work
  with this semester is text. The most common approach to dealing with
  large bodies of text is statistical, which requires counting the
  number of words in a document.
<br />
Write a Python function that can take a string as input and create a
  dictionary that maps each word in the string to the number of
  times it occurs in the string. The function should provide the user
  with the option of converting all words to lower case and also
  stripping off punctuation.

  You should also provide a "main" method that takes command-line
  arguments indicating whether stripping or conversion is desired, as
  well as the name of a file to use as input. It should also provide
  the user with the ability to pickle the dictionary to a file for
  later use. 

(30%) Graphs. Graphs are one of the most commonly used data
  structures in computer science. In this assignment, we'll represent
  a graph as an <a
  href="http://en.wikipedia.org/wiki/Adjacency_list">Adjacency
  list</a>. This will be implemented as a dictionary that maps a
  vertex to a list, which contains each of its neighbors, along with
  associated data such as edge weight.
<br />
<ul>
 <li> To begin, write a Python program that can read in graph data as
  provided in the sample inputs and construct an adjacency list. For
  each edge in the graph, there are two numbers: distance and travel
  time. Both should be stored in a tuple, along with the destination
  vertex. </li>
  <li> Next, implement a method that computes <a href="http://en.wikipedia.org/wiki/Floyd-Warshall_algorithm">all-pairs shortest path</a>
  on the graph. it should return a 2-D matrix, implemented as a list
  of lists. The link above contains pseudocode for the Floyd-Warshall
  algorithm, which you should use.
</li>
<li> You should also provide a main that takes as input the name of
  the input file, whether all-pairs is to be computed, and whether the
  graph should be pickled and stored in a file, or else printed to
  standard output. </li>
<li> Sample inputs can be found here. This is geocoded data
  representing actual waypoints and distances in San Francisco.
  
  In this problem, you'll learn some basic concepts surrounding
  machine learning, specifically how to construct training and test
  sets, how to test an algorithm, and how to measure performance.

  load breast cancer dataset.

  train on DecisionTreeClassifier.

  next, use train_test_split to do 5-fold and leave-one-out
  validation.

>>> X, y = datasets.load_breast_cancer(return_X_y=True)
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
>>> cl=tree.DecisionTreeClassifier().fit(X_train, y_train)
>>> scores = cross_val_score(cl, X, y, cv=5)
>>> scores
array([0.9122807 , 0.92105263, 0.92105263, 0.94736842, 0.91150442])
>>> scores = cross_val_score(cl, X, y, cv=5, scoring='average_precision')
>>> scores
  array([0.92245039, 0.91321761, 0.91989687, 0.94981174, 0.92559672])

  explain precision and accuracy.


  also, modeling of environments:

  - Chatbot

  - Autonomous vehicle driving around SF

  - Trash-sorting agent

  - Recommender agent. 




