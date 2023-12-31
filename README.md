# _Hangman'os'_

Hangman'os' is a pure Python language program, running in Code Institute mock terminal deployed on Heroku.

Feel free to challenge yourself in this nostalgic game, while using your memory and your deduction skills to guess the mystery word in classic Hangman game.

  ![Mock Up](/assets/images/Mockup.png)

## How to play

The game consists of a simple Hangman game, well-known for most of us, being present day by day in our childhood. As a brief resume of the game, we can say that is a word guess game with six attempts to win, in this project the computer gets a random word from a pre-defined list, and display to the user as underscores showing just its lenght, the user can guess a letter or the whole word, whenever the user entered the wrong letter, will be displayed for him, the head, after the torso and so on, otherwise if he guesses the right one, the corresponding letter and its position on the word will be displayed for him.

## Features

### Existing Features

- __Random Word Generation__
 
  - A message to welcome the user to the game is displayed.
  - The gallows pole is displayed to the user.
  - The user can see the word length and the mystery letters are displayed as underscores.

  ![Land Page](/assets/images/Start-Page.png)

- __Guesses Conditions__
 
  - The user can guess the letters according to the following conditions:
    - Only alphabetic characters are inputted.
    - Only one letter per turn or the word itself.
    - Only new guesses, assuring the user did not input the same letter again.

  ![Guesses Conditions](/assets/images/Guesses-Conditions.png)

- __Right Guesses__

  - If the user guess the letter, the letter would be shown in its corresponding position at the word, even if the letter occurs twice at the word.

  ![Right Guesses](/assets/images/Right-Guesses.png)

- __Hangman Stages__
 
  - The hangman stages is just the visual feedback of how many attempts are lefting.
  - Each time the user guesses wrong, a part of the hangman will be drawn, first the head, then the torso, arms and finally the legs, ending the game.

  ![Hangman Stages](/assets/images/Hangman-Stages.png)

- __Game Over Menssage__
 
  - When the game is over, as a result of the user running out of attempts or the correct word is guessed, a message with the user result will be displayed, and then the mystery word will be revealed.
  - Lastly, the user will be asked if he would like to keep playing or not, if he does want, then a new word will be picked, restarting the game, otherwise the game will exit, just the letters 'y' or 'n' will be accepted as a input, lower or upper case.

  ![Game Over](/assets/images/Game-Over.png)

### Features Left to Implement

  - Allow the user to get a hint to guess the word.
  - Allow user to choose the dificulty, easy, medium or hard.
    - In the easy mode, the first letter is shown.
    - In the medium mode, no special rules will apply.
    - In the hard mode, the user starts with the head, torso and arms drew, leaving just two attempts to guess the word.

## Testing

  - I have tested the code by the following methods:
  - Passed on the validator code PEPE8, no issues found.
  - I manually tested the code, passing invalid inputs, such as, more than one letters, numbers, spaces, special characters etc.
  - I tried all possibles ways to win or lose the game, and no bugs were found.
  - The game was tested on Heroku terminal and on the local terminal.

## Validator Testing

  - No errors were returned when passing through the official [PEP8](https://pep8ci.herokuapp.com/) validator.

  ![PEP8 Validator](/assets/images/PEP8.png)

## Bugs

### Solved Bugs

  - When I wrote the function to check if the guess was in the word, the code unexpectedly appended two characters in the same index list, if they both were in the word, causing me a problem to evaluates when the game was finished, that error occurred because I allowed the user to input two characters strings as a guess, the solution was to accept only the whole word or one single character.
  - When I fixed the bug described above, I didn't get the expected logical result when I inputed the word to be guessed, that happened because I was checking if the user inputted only one letter before checking if the user had guessed the whole word, in other words, was a flow bug.

### Reaming Bugs
  
  - No bugs reaming

## Deployment

  - This project was deployed at Heroku, steps for deploy are listed bellow:
    - Fork or clone the repository.
    - Creat a new Heroku app.
    - Set up the configs for the deployment.
    - Link the Heroku app to the repository, then Deploy.

    - The live link can be found here: [My Game](https://hangmanos-42ee37923464.herokuapp.com/)

## Credits:

  - I was inspired by the design of the gallows pole and hangman stages, by the code of Darren.
    - [Darren-Source-Code](https://gist.github.com/lupinetti/8f89e5f33750aa7c91c3)
  - I also watched some tutorias to get me inspired to write this code by my own.
    - [Kite-Video-Tutorial](https://www.youtube.com/watch?time_continue=4&v=m4nEnsavl6w&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dhangman%2Bpython%26sxsrf%3DAB5stBhnXzgtckX52y8XSx9C0_G0PC5iTQ%253A1688506312853%26ei%3DyI-kZL_dM7KYhbIPxIaPs&source_ve_path=MjM4NTE&feature=emb_title)
    - [Shaun-Video-Tutorial](https://www.google.com/search?q=hangman+python&sxsrf=AB5stBhnXzgtckX52y8XSx9C0_G0PC5iTQ%3A1688506312853&ei=yI-kZL_dM7KYhbIPxIaPsAE&ved=0ahUKEwi_4emXgPb_AhUyTEEAHUTDAxYQ4dUDCBA&uact=5&oq=hangman+python&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCMQigUQJzIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLAToECAAQRzoKCAAQRxDWBBCwAzoECCMQJzoICC4QgAQQywFKBAhBGABQjRBYgBZg5hZoAXABeACAAVaIAa4DkgEBN5gBAKABAcABAcgBCA&sclient=gws-wiz-serp#fpstate=ive&vld=cid:fee61799,vid:pFvSb7cb_Us)
  - I also searched for solutions of the problems that occurred during the project development on the following websites:
    - [Stackoverflow](https://stackoverflow.com/)
    - [Geeksforgeeks](https://www.geeksforgeeks.org/)
    - [Freecodecamp](https://www.freecodecamp.org/news)
  - The Code Institute for the deployment terminal