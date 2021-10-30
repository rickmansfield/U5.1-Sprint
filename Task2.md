# Unit 5.1 Task 2 

## U.P.E.R Summary
- import bulitins to view in my vscode ide
- print and explore found reversed!
  - reversed() reversed(sequence, /)
 |  Return a reverse iterator over the values of the given sequence.
- construct basic fucntion with def and return
- create a variable to hold the reversed(str) method results
- return variable with .join() to reconstruc the iterations into a single string. 
  
## Note
    at first I could not see the reversed() results So I went back and found next()
    next(...)
    next(iterator[, default])
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    this helped me realize the reversed() was retruning the individual chars and I needed to employ .join() to reconstruct the final version. 