# arithmetic_arranger

# What it does

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----


# Example inputs and outputs

## Without results 

input: 

["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

## With results:

input: 

["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True

output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474


### The idea for the project and testing environment from freeCodeCamp - https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter