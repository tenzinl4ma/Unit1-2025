<h1 align="center" >Todo List</h1> 

# Criteria A: Planning

## Problem definition

Zamir, the client, is a young social media influencer who take a lots of the photos and post in many social media platform like Tiktok, Instagram and Facebook. He start his passion since he was middle school student and till these days his passion has never faded. He wanted to be a great influencer and has wide friend zone where they share a lots of thing, but the problem is they also share the phone with eachother, even though he trust his friend 100%, he doesn't trust the situation upcoming. We never know what will happen coming days, so he want a product that manage all social media and important passwords that is  well hidden like in vault that doesn't look like a password managers and, no unathorised person could access it.

There is no such existing product that meets Zamir's requirement, allowing him to store and manage his password well hidden. So, is in need of someone who is capable of developing such app that fulfill his requirments. A developer Tenzin Lama, agrees to develop a product that meets his requirements, allowing him to manage and store the password of his social media account that is well hidden behind other app.

Moreover he is open to any additional function or customization that developer will add.

## Proposed solution

Design statement: I will create a **To-do list app** for a client who is **Zamir**. The **To-do list** will be an **simple terminal application that can only access and run through terminal** and will be developed by **PyCharm** code editor. It will take **two weeks** to finish and will be evaluated according to the criteria **A, B, and C**.

### Introduction to the Encryption: 
In this product developmet process the encryption is very important to know for both developer and client side. Encryption is the method of securing your data and information into some other form that is unable to read and understand by the intercepter until its decrypted with corrected code. People often have misconception of believing that encryption and password is same, but ther is huge difference between them is that password is plain text if someone know it they can use it to access but encryption is a encoded form that even one know it they won't be able to use it till they decrypt it.


## Design Statement(rationale):
The product will be developed on the popular python Integrated Development Environment called PyCharm software which is developed by Czech company Jetbrain which has wide range of essential tools that helps developers to cuztomize and add the desired functions. I also has lots of plug-in and shortcuts which enables developer's to developed efficiently providing developer friendly environment. This IDE best fit for the developer to achieve the goals that the client has set and shorten the time compare to other software.

Some important features of this product include: a terminal based interface to-do list application that is capable of adding the multiple tasks, viewing the text and removing the tasks, it also shows the user friendly error message 'invalid input' if input is incorrect. It function as normal to-do list. It provide a warm and user friendly welcome message and also accept a **secret code** from user, if secret code is input, it will ask for password. If the user input the incorrect password for thrice the system will no longer take the keyboard and mouse input, completly locking the system till you swap the window. However the user input correct password it will show all the encrypted password in decrypt form. After, entering the password file you can add, delete the password list. All these function and completed app frame provide and fulfill the clients demands.


## Success criteria

1.The To-do list is a text-based software (Runs in the Terminal).

2.The To-do list is capable adding, viewing and removing the tasks.

3.The To-do list shows user friendly message when doing the operation .

4.The To-do list accept secretcode and password from user and direct them to the password manager.

5. The password saved in tsv.file is encrypted form and will be decrypt when its open through password manager.

6. In password manager you can retrive, add, remove the password which will also changes will take place in original file.


# Criteria B: Design

#### System Details

<img align="left" width="445" alt="Screenshot 2024-09-23 at 23 17 33" src="https://github.com/user-attachments/assets/0b04e11a-1c14-4ad3-85f7-7639bd9ecf40">

### The system details
##### **pwd** shows the current working directory and <br>**ls -l** shows the list of all the files inside that directory <br>with the date modified <br>**python3 --version** show the version of python installed in <br>system and the **system_profiler SPHardwareDataType**<br> shows the system software details.<br clear="left"/>
----------------------------------------------------------------------------------------------------------------------------------------

## **Fig-1** The System Diagram

<img width="900" align="center" alt="System diagram" src="https://github.com/user-attachments/assets/bf0aba54-4440-46a9-81dc-2dacc89b3446">






## Flow diagrams












## Record of tasks
| Task Number | Planned Action                                            | Planned Outcome                                                              | Time estimated | target completion date | Criterion |
|-------------|-----------------------------------------------------------|------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st meeting with client                                   | obtain a problem defination understand the situation                         | 10 min         | sep 7                  | A         |
| 2           | Brain-storm and propose  solution                         | jot down the ideas and  solution                                             | 25 min         | sep 8                  | A         |
| 3           | choose the system and IDE                                 | To choose the best fit hard- ware and software for deve- loping the products | 15 min         | sep 10                 | A         |
| 4           | flowchart and diagram for To-do list and encrypted  files | To create the best solution                                                  | 30 min         | sept 12                | B         |
| 5           | Alpha Development                                         | Code first draft of the program that meets client demands                    | 12 hrs         | sept 15                | C         |
| 6           | Beta Testing                                              | Trace and find the bugs, errors, by testing with users                       | 2 hrs          | sept 18                | A         |
| 7           | Beta Development                                          | Fix the bugs, errors and  add more functionalities.                          | 9 hrs          | sept 20                | C         |

## Test Plan
| Task Number | Planned Action                                            | Planned Outcome                                                              | Time estimated | target completion date | Criterion |
|-------------|-----------------------------------------------------------|------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st meeting with client                                   | obtain a problem defination understand the situation                         | 10 min         | sep 7                  | A         |
| 2           | Brain-storm and propose  solution                         | jot down the ideas and  solution                                             | 25 min         | sep 8                  | A         |
| 3           | choose the system and IDE                                 | To choose the best fit hard- ware and software for deve- loping the products | 15 min         | sep 10                 | A         |
| 4           | flowchart and diagram for To-do list and encrypted  files | To create the best solution                                                  | 30 min         | sept 12                | B         |
| 5           | Alpha Development                                         | Code first draft of the program that meets client demands                    | 12 hrs         | sept 15                | C         |
| 6           | Beta Testing                                              | Trace and find the bugs, errors, by testing with users                       | 2 hrs          | sept 18                | A         |
| 7           | Beta Development                                          | Fix the bugs, errors and  add more functionalities.                          | 9 hrs          | sept 20                | C         |

# Criteria C: Development


your code


```.py


my python code


```



## lib imported code


```.py


inmported code

```

## My lib
my color and validation library

```.py
my library

```






Sources:<br>
w3school:"https://www.w3schools.com/python/python_classes.asp"<br>
youtube tutorial:"https://www.youtube.com/watch?v=vsLBErLWBhA"<br>
MDN:"https://developer.mozilla.org/en-US/docs/Web/HTML"<br>
To-do:"https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814"<br>


