# PHYS20161 1st assignment: Bouncy Ball
September 6, 2022


## Introduction-to-Programming-Assignment-1

## 1. Analytic approach:

We can calculate the number of bounces analytically using conservation of energy. 
At height h the ball will have a potential energy of mgh, where the symbols have their usual meanings. 
After one bounce the ball reaches a height hη (0 < η < 1) where η takes into account energy lost during each bounce (an efficiency if you will). 
After a second bounce the ball will reach a height hη<sup>2</sup>, and so on.
We can find the number of bounces above some minimum height, h<sub>min</sub>, by examining the energy loss:

<div align="center"><code><i>mgh<sub>min</sub> = mghη<sup>n</sup></i></code></div>

where n represents the number of bounces.

## 2. Expectations:

Given user input for the initial height, minimum height of interest, and η; we expect your code to
be able to calculate the following:
- The number of bounces over h<sub>min</sub>, n, where n ≥ 0.
- How many seconds it takes to complete the bounces.

As an example, the ball makes two bounces over h_min and the time taken to complete these, t, is slightly below 5 seconds. If the ball makes no bounces over h<sub>min</sub>, you should still output the time of this drop; the zeroth bounce.

We will also be marking you on programme style and expect your code to contain:

- A clear header with title, author, date and purpose of the code.
- Appropriate spacing to break up the code as per the style guide.
- Useful functions that break up the calculations and make the code modular.
- Unambiguous variable and function names.
- Results outputted clearly; the number of seconds should be quoted to two decimal places and the number of bounces is an integer.

We will award additional marks based on how well written the submission is and if it can provide any additional information. For instance, does it validate any of the input variables? Does it validate them well? Can it calculate anything else? Can the user decide this? Does the code get a positive linter score?

<div align="center">
<img src="https://user-images.githubusercontent.com/9414661/194276833-1c3d5eee-b801-44e6-afa1-e503e4ed76e5.png" alt="drawing" style="width:400px;"/>
</div>

## 3. How to Download and Build Project:

To run this project you will need Python 3.10 or later installed.
Just go to the main page of this repo and download the code.
Once you have the code in your local machine you can just run the batch (Windows) or the shell (Linux and Mac) file provided to setup your virtual environemnt.

Just run ```prep-venv.bat``` on Windows or ```prep-venv.sh``` on Linux or Mac.

The script should also install all the required packages in the virtual environment.

Once the environment is set just run the following command: 

```
python main.py
```
