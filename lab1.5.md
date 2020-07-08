Lab 1.5
---------
In this lab, you will get familiar with the basic usage of `git` and Github.

# Step 1: Cloning from the Github repository

1. Go to `https://git-scm.com/downloads` and download `git` for your computer.
2. In your terminal, enter `git --version` to check if it is installed correctly.
1. Go to the repository for this class at `https://github.com/Yiluo-pHoton/MAST_Brian_Python`. This is where you will see your code being uploaded.
2. Now on your own computer, open up a terminal and go to a directory that you want to put these codes in (for example `Desktop`)
3. Enter `git clone https://github.com/Yiluo-pHoton/MAST_Brian_Python` and the code should start downloading.
4. `cd` into `MAST_Brian_Python` and create a directory here using `mkdir brian_code`
5. After you finish `lab1`, move your `lab1` folder with all the code inside to `brian_code`
6. In your terminal, go to directory `MAST_Brian_Python` and enter `git status`
7. You should be able to see `brian_code` listed with red color
8. Now enter `git add .` and do `git status` again
9. This time you should see `brian_code` listed with green color
10. Enter `git commit -m "lab1 code"`, where you could enter something else for `lab1 code` part
11. Finally enter `git push`
12. Terminal will ask for your Github username and password. After you enter those, you should be to see that your code is pushed to the Github repository
13. Go to the repository for this class at `https://github.com/Yiluo-pHoton/MAST_Brian_Python` to check if you can see your code successfully pushed
14. Note: everytime when you try to push new code to the repository, don't forget to do `git pull` first to get the most updated code on the master branch
15. You could read more about how to use `git` and how it is used for software development by Googling, or maybe this is a good one: `https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners` 