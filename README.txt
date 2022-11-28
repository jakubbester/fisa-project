Title:      Project #2 (FISA Projects)
Authors:    Alex Shi & Jakub Bester

Description:

This project models the definition of "Electronic Surveillance" as defined in "50 USC 1801 (f)".
It works by interfacing with WebSpass and injecting a Spass script into the input textarea. Afterwards,
it runs the code and parses the result to display whether or not a particular scenario 

How to Run:
    1. pip install -r requirements.txt          : to install all of the required packages
    2. python fisa.py                           : to run the website
    3. ctrl + click link                        : to display the website (should be something like:
                                                                                "Running on http://127.0.0.1:5000")
    4. submit the desired inputs by filling out the form
    5. Selenium will walk user through submission of Spass formatted file with edits modified within.
       User simply follows and scrolls around if they would like to view the script.
    6. result is displayed at the bottom

Notes/Explanation:

In order to run the program, please run the command "python fisa.py" and a local server should be launched 
hosting the website were inputs can be made. After selecting all of your desired inputs, press the
submit button at the bottom, and a notification regarding that status of the input should appear.

Challenges/Difficulties
    1. We began by using z3 in order to solve for whether or not the scenario fits the definition.
       However, we ended up switching to using Selenium and interacting with WebSpass directly
       (even though it is rather inefficient)
            This can be seen from the "50 USC 1801 (f)-z3.txt" file that is present.
    2. There were several minor challenges in implementing the final code. Specifically, there
       were several obstacles to deal with in regard to Selenium with the code timing out and
       it not injecting the full required file
    3. There were sevearl minor logical errors made in coming up with the final model
       for defining "Electronic Surveillance."
    4.In defining the model, we ran into problems around fuzzy language. For instance, whereas (3) very clearly
       states that intent is important, the other 3 definitions do not mention this term explicitly, but it seems
       to be inherently implied.
    5.Moreover, there are definitions such as "reasonable expectation of privacy" that
       were difficult to translate and ended up being taken as primitives that do not confer their complexity.
    6. For the front end itself, there were challenges in
       constructing questions that would not misrepresent anything. For instance, one of our questions is
       "Was the acquired information only the relevant information?" but this questions was supposed to represent
       (iv) of section2511 which is "such interception does not acquire communications other than those transmitted
       to or from the computer trespasser."