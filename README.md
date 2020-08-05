# CS662 Assignment 1

 ###Due Date: Aug 31.

In this assignment, you'll characterize some AI problems according to the different parameters presented in lecture and in the text. 
This assignment is also meant to get you up to speed with Python, build a
couple of tools that we'll use later in the semester, and also give
you an early taste of machine learning using scikit-learn. For all
assignments, you must use the provided template code as a starting
point.

You are expected to follow best practices in terms of software
development. In other words, please make your code easy to read and
understand. In addition, you are expected to provide a README
describing how to run your code, and a simple test script.

1. (25%) Problem characterization. For each of the following AI problems, describe the modeling choices you. would make, including:
* Environment - is it best modeled as discrete or continuous, static or dynamic, deterministic or non-deterministic, and episodic or sequential.
* Online or offline? 
* How important is it that our agent's actions be explainable?
* Will our agent need to reason about other agents?
* How will we describe and measure success?
* Will our agent need to learn? If so, what data and feedback will be available to it?

Please place your answers in a Word or PDF document added to your repository for this assignment.

* An intelligent chatbot. We would like to build an agent that can intelligently communicate with users in a text-based chat setting. It should be able to talk about a variety of subjects and carry on a dialogue.
* An autonomous Uber/Lyft. We would like to build a self-driving car that can safely navigate the streets of San Francisco and pick up and drop off passengers.
* A trash-sorting agent. We would like to build an agent that can observe pieces of trash as they pass by on a conveyor belt and identify them as recyclable or not. 
* A class-scheduling agent. We would like to build an agent that can take each student's preferred courses and find the optimal schedule for all students.


2 (25%) Word frequencies. One of the primary domains we'll  work
  with this semester is text. The most common approach to dealing with
  large bodies of text is statistical, which requires counting the
  number of words in a document.

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

(25%) Graphs. Graphs are one of the most commonly used data
  structures in computer science. In this assignment, we'll represent
  a graph as an [adjacency list](http://en.wikipedia.org/wiki/Adjacency_list). This will be implemented as a dictionary that maps a
  vertex to a list, which contains each of its neighbors, along with
  associated data such as edge weight.

* To begin, write a Python program that can read in graph data as
  provided in the sample inputs and construct an adjacency list. For
  each edge in the graph, there are two numbers: distance and travel
  time. Both should be stored in a tuple, along with the destination
  vertex.
*  Next, implement a method that computes [all-pairs shortest path](http://en.wikipedia.org/wiki/Floyd-Warshall_algorithm)
  on the graph. it should return a 2-D matrix, implemented as a list
  of lists. The link above contains pseudocode for the Floyd-Warshall
  algorithm, which you should use.

 You should also provide a main that takes as input the name of
  the input file, whether all-pairs is to be computed, and whether the
  graph should be pickled and stored in a file, or else printed to
  standard output. 
 Sample inputs can be found here. This is geocoded data
  representing actual waypoints and distances in San Francisco.
  
 (25%) Machine Learning. In this problem, you'll learn some basic concepts surrounding
  machine learning, specifically how to construct training and test
  sets, how to test an algorithm, and how to measure performance.

For this problem, we'll be using
[Scikit-learn](https://scikit-learn.org/stable/index.html). Scikit-learn
is a large and popular open source Python package for machine
learning, primarily supervised batch learning. We'll just get our feet
wet here and see how to evaluate a machine learning algorithm. The
information that you need to complete this task can be found in the
scikit-learn tutorial and API documentation.

To begin, we will need a dataset. We would like to use the
[breast cancer dataset](https://scikit-learn.org/stable/datasets/index.html#breast-cancer-dataset). This
dataset contains 569 instances, each with 30 measurements done on
tumors, along with a classification (malignant or benign). The
learning problem is to predict a tumor's class from the observed
characteristics.

Modify the getDataset() function to load the breast cancer dataset,
rather than the iris dataset.

Next, we will need a classifier. For this, we'll use a built-in
classifier called a _decision tree_. Later in the semester you'll
implement this yourself, but for now we'll just use this one. Modify
the dtTrain() function to _fit_ the tree to the data. Assume that you
will use all the data provided to the function to fit the tree. (check
the scikit-learn API for the DecisionTreeClassifier for the fit()
method.)

To begin, fit the tree to the entire dataset. Then test your results
using the predict() method.

Your tree should classify everything correctly. If we think about it,
this shouldn't be a surprise - all we're asking it to do is to recall
the data it's memorized. What we really want to know is how well the
classifer does on new data that it _wasn't_ trained on.

To do this, we'll train on a subset of the data, and then test on the
rest. This is called _cross-validation_.The number of subsets of the
data set we hold out are referred to as folds. So, in 5-fold
cross-validation, we would break the dataset into five subsets, train
on 4 of those and test on the fifth, and then average the results. Complete the fiveFold()
method to implement this.

Lastly, we need to think a little about how to measure our
performance. Counting misclassified examples is hard to interpret
without knowing how large the dataset is.

Let's instead compute _accuracy_, which is the percentage of
examples that were classified correctly. Modify FiveFold to compute this.

It would seem that training on more data would make our tree more
accurate. Verify this by using scikit-learn's _cross_val_score()
method to test your classifier's performance with 5,10,20, and 50-fold
cross-validation. Include a table in your writeup with the results of
this experiment.










