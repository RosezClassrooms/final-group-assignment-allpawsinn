[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=341481&assignment_repo_type=GroupAssignmentRepo)
# Group-Assignment
This is the final group assignment for the semester. For this assignment you are required to use two design patterns that were covered post midterm.

They can be used in two separate problems, on using each, or in the same problem that require both.

Please select a problem/problems that are managable with regards to successful implementation.
When submitting your repository, please edit this readMe file to clearly describe the applications you have designed and mention what patterns you have chosen to you for them.


#Patterns:
We chose builder and facade patterns

#Builder pattern:
For the builder pattern, we assumed we are car retailer and to provide customers to better service we preapared a program that is responsible for creating cars in different circumstances.For example, if customer wants to buy Racing car, he/she can customize the car with a few options like brand, horse power, engine, color etc.

#Why builder pattern?
We choose builder pattern to develop car shopping application because according to our application users should able to create different representations with same construction process. If we did not choose the builder pattern, we would have to create a different car construction method for each representation, which means we do a lot of repetitions on our code. In addition, whenever the car seller added a new feature, we had to change our code for each added feature. With the help of builder pattern, we make our program automatically extensible.

#Facade pattern:
For the facade pattern, we implemented a computer system platform that have the main components in the pc, CPU, GPU, RAM and Power Supply. Our system simulates a PC that you can start it, boost the components' frequency, print the results and if the existing power supply is not enough to run the PC. You can change the PSU in order to build a fully functional PC.

#Why Facade pattern?
A computer has a complex subsystem that contains lots of unique parts, like CPU, RAM, GPU etc. However in order to run a powerful pc you need a decent power supply unit to deliver enough power to sysyem. Façade pattern exactly solves that problem for us, our program deal with lots of complex parts with unique features however the client only deals with simple things that client only cares about. While each part has many different features to choose, a client generally only cares about whether pc is running or not. 

#Note to Professor:
 Before you cancelled the strategy pattern homework, we were completed it. If you can check it we did it right or not, it would be so benefical.
 
#Instructions:
in order to run different pattern these run command can be copy and paste to .replit
run = "python3 car_builder.py"
run = "python3 pc_facade.py"
run = "python3 strategy_patern.py"
