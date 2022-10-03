# learn-swedish

This is a Flash Card App Capstone project for learning swedish using Tkinter and pandas.

The source for the swedish sentences is extacted from the repository https://github.com/hermitdave/FrequencyWords, therefore, a converter is needed to only extract the interesting lines in the txt file.
The converter is using CVS library to loop through the lines and create "to_learn" file which antains only the english sentence and it's translation.

The flash card app chooses a random sentence and checks if you knew the translation or not, if clicked ✅, the sentence will be autumatecally deleted from "to_learn" file and will not show up again.
If the user chooses ❌, the sentence will not be removed and therefore will show up again randomly.

![example-project](https://user-images.githubusercontent.com/97854234/193567321-c924cc33-5dff-4152-9d2b-095332ca08a4.png)
