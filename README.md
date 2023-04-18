Jason Rossi jrossi3@stevens.edu Saicharan Saini ssaini1@stevens.edu

https://github.com/Jrossi3/CalculatorLanguage

Jason and Saicharan spent approximately 40 hours each on this project.

# Testing
The way we tested our code was through the input testing with pressing control d to end the code. One instance was we would input "print 1" then press enter then input "print 2" then press enter and then press control d. This would return 1.0 and 2.0 on separate lines. Any errors we would get, we would trace through our code to fix it. We would also use commas in our print statements to allow for multiple inputs for print.

# bugs and issues
There were a couple bugs and issues we could not resolve. One being allowing for multiple inputs with ++ and --. We also could not solve how to do comments where there could be x = /* \n \n \n */ 5 and then print x would return 5. We also struggled to completely fine tune the boolean operations as we kept getting "D" with the output if we only had one output. So "print 1&&2" would give "1D" but "print 1&&2, 1&&3" would give "1.0 1.0". 

# resolved issue
A difficult issue we solved was altering our code so that control d would end it instead of pressing enter for a second time without any input. This took a lot of time as we had to use STDIN and figured out how to end the code at the correct times without causing any issues. This was also difficult because it meant we had to create a dictionary that would be the output of the code for everything. So we had a global counter to keep up with the different keys. This was a lot because we had to then rework our main function a great deal and move a lot of code around whilst still keeping the rest of it intact. 

# Four Extensions
1) Comments
Positive Examples:

    input:
    x = 5
    /* 
    x = 2
    */
    print x

    output:
    5.0

    input:
    x = 1
    /* 
    x = 2
    y = 3
    */
    y = 4
    # print 0
    print x, y

    output:
    1.0 4.0

Negative Examples:

    input:
    x = /*
    a = 2
    b = 3
    c = 4
    /* 5
    print x

    output:
    parse error

    correct output:
    5.0

    input:
    x = /**/ 3        
    print x

    output:
    parse error

    correct output:
    3.0

2) Op-equals
Positive Examples:

    input:
    print 1<2

    output:
    1.0

    input:
    print 1<2, 2<1

    output:
    1.0 0.0

Negative Examples:

    input:
    x = 1
    print x, 1<2

    output:
    1.0 1.0 2.0

    input:
    y = 2
    print 1<2, y

    output:
    1.0 2.0 2.0

3) Relational Operations
Positive Examples:

    input:
    x = 3
    x *= 2
    print x

    output:
    6.0

    input:
    x = 10
    x += 2
    print x

    output:
    12.0

Negative Examples:
N/A

4) Boolean Operations
Working Examples:

    input:
    print 1&&2, 1||2, 0||0, 0&&5

    output:
    1 1 0 0

    input:
    print 1&&-1, !2, 1&&0, 2&&5

    output:
    1 0 0 1

Negative Examples:

    input: 
    print 1&&2

    output:
    1D

    input: 
    print 0&&2

    output:
    0D
