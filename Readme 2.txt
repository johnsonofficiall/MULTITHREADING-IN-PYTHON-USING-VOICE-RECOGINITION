                                         MULTITHREADING In PYTHON USING VOICE RECOGINITION
OBJECTIVE:
        We just implement the multithreading concept in Python program using voice recogition.

REQUIREMENTS:
         #tk
         #pyaudio
         #pyttsx3
         #speechrecognition
PROCEDURE:
    1)create a new python environment and install the requirements in the python environment.
    
    2)Go to the folder where the script file or folder in the newly created environment.
 
    3)open command promt in the current path.

    4)Activate the  python environment in the command prompt.

    5)Run the python file in the Activated environment.

EXPLANATION:
     It is a python program for multi threading using voice recoginition.Multithreading is the ability of a program to enable more than one user at a time without requiring multiple copies of the program running on the computer. Multithreading can also handle multiple requests from the same user.
   
     The Main overview of the program is whatever the person who speaks in english ,the program recoginizes it and convert it into a text and store it into a desired text file what we chooses.
 
     The time Library is necessary for to import in the program for to know the time when the program is strats to execute or when it gets ended or to get the current time of the executing program.The time will display in the top right corner while the program is running.speech recognition and pyttsx3 libraries for the recoginiton of the speech when the program is being running and  convert it into a text.for these purposes,these libraries are necessary to implement.

    when we run the program three things  happen in the output window, 
              1)It shows the time at the top right corner which refers to the program execution timing.
             
              2)The background color will changes alternately corresponds to the time which means when the time differs, color changes according to it.
             
              3)The third one is the trivial thing which is supposed to be a game changer.when the program starts to begin, when a person or a thing speaks in english at the time of the speech, the program gets its audio and recoginizes  and understands it.The recoginized speech or audio will be converted into a text by the program.these text will be converted into a log file(txt file).For the file creation,we just given a code for path of the file.

   You may have the question what is the stopping condition of the program or how long will it recoginizes the speech and convert it?
                  First of all we'll tell you that it is a simple GUI program.The stopping condition is depends on the GUI interface.when we run the program a GUI interface will also be opened simultaneously where we used the multithreading.The user who wants to stop the program means he simply needs to close the GUI interface which was opened or created when we executed the program.The audio will be converted into a text till the GUI was closed.hence to stop the program the GUI should be closed.
   
  In the future we also like to build a AI model and attach it with the project we made and also with an AI chatbox.
   

  