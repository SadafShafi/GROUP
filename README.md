
![GitHub Logo](https://github.com/SadafShafi/GROUP/blob/main/images/dedabc81-4260-491a-b121-7a9a29026704_200x200.png)


# GROUP

In mathematics, a group is a set equipped with a binary operation that combines any two elements to form a third element in such a way that four conditions called group axioms are satisfied, namely closure, associativity, identity and invertibility. One of the most familiar examples of a group is the set of integers together with the addition operation, but groups are encountered in numerous areas within and outside mathematics, and help focusing on essential structural aspects, by detaching them from the concrete nature of the subject of the study.
### As a Data Structure:

We can use a group as a data structure where we can have our generic set of elements on which we can have certain operations we want and get the output from the same set of elements.
Groups are widely used in Sciences and Mathematics.
For example , we can represent the motion of objects along certain axis, we can represent the motion and spin of electrons etc.

#### Nerdy Details:

[Wiki](https://en.wikipedia.org/wiki/Group_(mathematics))

#### Non-Nerdy Details:
[Youtube](https://www.youtube.com/watch?v=g7L_r6zw4-c)

### Dependencies:
 multipledispatch

  **pip install multipledispatch**
  
  
### To install:

**pip install ____**

### Example:

## #1 :
Say we have a clock which only keeps track of 4 hours, so we have a set of 4 numbers only and when we run any operation on our new set of numbers we can expect the output from the same set.

<img src="https://github.com/SadafShafi/GROUP/blob/main/images/autodraw%2010_1_2020%20(1).png" alt="drawing" width="200"/>

    >>from GROUP import Group
    >>obj = Group([0,1,2,3],pointer=2)
    >>obj.step()
    >>3
    >>(3*obj).step()  #3 steps at a time
    >>1
    >>obj.step(pointer=3)
    >>0
 
This piece of code simulates the working of the above clock


## #2:
Now lets simulate the behaviour of the following traingle, which can rotate and stip on its axis
<img src="https://github.com/SadafShafi/GROUP/blob/main/images/autodraw%2010_1_2020.png" alt="drawing" width="600"/>

    >>from GROUP import Group
    >>obj = Group([[1,2,3],[2,3,1],[3,1,2]],pointer=[1,2,3],[[1,3,2],[3,2,1],[2,1,3]])
    >>obj.step()   #rotate the triangle
    >>[2,3,1]
    >>obj.switch()  #spin the triangle
    >>[3,2,1]
    >>(2*obj).step() ##rotate 2 times
    >>[1,3,2]
    
  
All the suggestions and changes are welcomed
Since Abastract Algebra is quite vast, this data structure has a huge scope of improvement

    
