# CMPSC 202 - Midterm Programming Assignment

Name: Luke Perez

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

*list your methodological errors and fixes here*
- Had input generation included in the measured time. -> It now generates each input before starting the timer, so the measured time reflects only the algorithm’s time.
- Used different random inputs for each algorithm -> It now runs both algorithms on the same input at each size, making the comparison fair.
- Tested only one input size and ran each algorithm only once. ->  It now tests several input sizes and repeat each measurement five times.
- Used time.time() instead of time.perf_counter() which is higher resolution and accuracy. -> time.time() was replaced with time.perf_counter()

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.




