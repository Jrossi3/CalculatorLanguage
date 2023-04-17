Jason Rossi jrossi3@stevens.edu Saicharan Saini ssaini1@stevens.edu

https://github.com/Jrossi3/CalculatorLanguage

Jason spent approximately 42 hours on this project.

# Testing
The way we tested my code was through the input testing with pressing control d to end the code. One instance was we would input "print 1" then press enter then input "print 2" then press enter and then press control d. This would return 1.0 and 2.0 on separate lines. Any errors we would get, we would trace through our code to fix. 

# bugs and issues
There were many bugs and issues we could not resolve. One being allowing for multiple inputs with ++ and --. We also could not solve how to do comments where there could be x = /* \n \n \n */ 5 and then print x would return 5. We also struggled to completely fine tune the boolean operations as we kept getting "D" with the output if we only had one output. So "print 1&&2" would give "1D" but "print 1&&2, 1&&3" would give "1 1". 

# resolved issue
A difficult issue we solved was altering my code so that control d would end it instead of pressing enter for a second time without any input. This took a lot of time as we had to use STDIN and figured out how to end the code at the correct times without causing any issues. This was also difficult because it meant we had to create a dictionary that would be the output of the code for everything. So we had a global counter to keep up with the different keys. This was a lot because we had to then rework my main function a great deal and move a lot of code around whilst still keeping the rest of it intact. 

# Four Extensions
1) 
