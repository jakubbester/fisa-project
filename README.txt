Title:      Project #2 (FISA Projects)
Authors:    Alex Shi & Jakub Bester

Description:

This project models the definition of "Electronic Surveillance" as defined in "50 USC 1801 (f)".
In order to run the program, please run the command "python fisa.py" and it should launch a local server
with hosting the website were inputs can be made. After selecting all of your desired inputs, press the
submit button at the bottom, and a notification regarding that status of the input should appear.

Notes:


Challenges/How to run/etc.
Challenges:
In defining the model, we ran into problems around fuzzy language. For instance, whereas (3) very clearly
states that intent is important, the other 3 definitions do not mention this term explicitly, but it seems
to be inherently implied. Moreover, there are definitions such as "reasonable expectation of privacy" that
were difficult to translate and ended up being taken as primitives that do not confer their complexity.
For the translation, we found it difficult to find a way to translate user responses from the front end
into formulae that a solver could understand. Finally, for the front end itself, there were challenges in
constructing questions that would not misrepresent anything. For instance, one of our questions is
"Was the acquired information only the relevant information?" but this questions was supposed to represent
(iv) of section2511 which is "such interception does not acquire communications other than those transmitted
to or from the computer trespasser."

How to Run:
Run "python3 fisa.py" in the terminal. Input specifications.