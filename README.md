# LAZY PROGRAM
#### Are you feel tired when you need to go through an open browser to open intra website or peer locate?
#### HERE'S THE SOLUTION

![image](https://github.com/wenjuin95/lazy_program/blob/main/Untitled.png)

1. i try to make a program that help me to open a website that i always visit with a click of button</p>
2. you need to put the link in the <b>custom.py</b> else it won't work</p>
> find this part
``` python
    def open_url():
	     webbrowser.open("[intra link]")-------_> replce [intra link] with your intra link
    def open_locatepeer():
      	webbrowser.open("https://locatepeer.vercel.app/")
    def open_slot():
      	webbrowser.open("[intra slot link]")--------> replce [intra slot link] with your intra slot link
    def open_github():
      	webbrowser.open("[github link]")------------> replace [github link] with your github link
```
 3. feel free to modify your own button</p>

## Requirements for this program
- python
- pip
- pyinstaller

## you have two option to install
### OPTION 1

1. check your pyinstaller does it exist
``` 
pyinstaller -v
```
3. if not exit try to install with pip
```
pip install pyinstaller
```
4. compile the install.py
```
python install.py
```
5. done (your exe file is in "dist" folder)

### OPTION 2
1. check your pyinstaller does it exist
```
pyinstaller -v
```
2. if not exit try to install with pip
```
pip install pyinstaller
```
3. (window: use power shell)now you can convert the python file to executable file
> replace "pyinstaller.exe path" with the path you get (example: C:\Users\[YOUR_USER_NAME]\AppData\...Scripts\pyinstaller.exe) and "your_script_name.py" is the name of your python file 
```
python [pyinstaller.exe path] --onefile [your_script_name.py]
```
3. (macos) (replace "your_script_name.py" with the name of your python file)
```
pyinstaller --onefile --windowed [your_script_name.py]
```
4. done (your exe file is in "dist" folder)
