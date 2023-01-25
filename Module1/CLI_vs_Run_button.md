# Command Line Interface vs. PyCharm's Run Button

These images show you how the text entries in PyCharm's Run dialog
relate to the Bash command line.

The foregoing images are color-coded:

| Color  | Meaning                                             |
|:------:|-----------------------------------------------------|
| Red    | The Python interpreter                              |
| Blue   | Your program written in the Python language         |
| Green  | Arguments to your Python program                    |
| Yellow | The current working directory of the Python program |


Suppose you run your program from Bash like this:

![cmdline.png](./assets/cmdline.png)


You may replicate this in PyCharm by using this configuration

![configuration.png](./assets/configuration.png)


As you run your program from PyCharm output is printed in the console.  The top
line of the console shows the command line that PyCharm ran on your behalf when
you pressed the *Run* button:

![pycharm.png](./assets/pycharm.png)
