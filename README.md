# DYNAMIC A2OJ
Easily track your ladder progress -> 
https://a2oj.herokuapp.com/

Since our all time favourite A20J ladders became static, my laziness to solve problems systematically took over me. Recently when I sat again to start solving problems the static ladder frustrated me a lot. I missed A2OJ a lot :-( and probably many of you guys also miss the dynamic A2OJ. Hence this, to help and motivate myself but eventually thought why not to share the fun.
https://codeforces.com/blog/entry/75669</br>


PS - I'm still not doing anything expect being lazy :-()

## For Contributors

#### How to install:
Refer to this video for better understanding of creating and activating virtual environment. ([See this video](https://www.youtube.com/watch?v=Wuuiga0wKdQ&t=61s))
- Create a folder (a20j-contribution)
- Create a virtual environment
```
py -m venv env
```
Now, you have to activate the environment.
* Go to the 'settings.json' in '.vscode' file and add and replace the path with the complete path of the 'Scripts' folder.
* In VS CodeTo get the complete path of 'Scripts' folder, click on the env folder (the name of your environment, in our case it's ```env```) and then right click on the 'Scripts' folder and choose "copy path" (not "relative path")
* It will look something like -> 
```
{
    "python.pythonPath": "C:\\Users\\username\\Desktop\\dynamic-a2oj\\env\\Scripts"
}
```
* In this way your environment will be activated.

- Cloning the repo
* Fork the repo
* Now, go 'a20j-contribution', and clone your forked repo (don't try to clone the main repo (subodhk01/a2oj)). Your cloned repo should be directly inside the 'a20j-   contribution' folder.
* Inside the 'a20j-contribution' type ```ls``` and you can see the 'env' folder and 'a2oj' folder.
- Installing all the dependencies(using requirements.txt)
* Inside the 'a20j-contribution'; type ```cd a2oj```. This will take you inside the your local repo of 'a2oj'. 
* Now, type ```pip3 install -r requirements.txt```. This will install all the dependencies mentoned in the 'requirements.txt' file. ([Help](https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project))
