<h1>LAZY PROGRAM</h1>
<h4>Are you feel tired when you need to go through an open browser to open intra website or peer locate?</h4>
<h4>HERE'S THE SOLUTION</h4>

![image](https://github.com/wenjuin95/lazy_program/blob/main/Untitled.png)

<p>1. i try to make a program that help me to open a website that i always visit with a click of button</p>
<p>2. you need to put the link in the <b>custom.py</b> else it won't work</p>
• find this part
<pre>
    def open_url():
	     webbrowser.open("[intra link]")-------_> replce [intra link] with your intra link
    def open_locatepeer():
      	webbrowser.open("https://locatepeer.vercel.app/")
    def open_slot():
      	webbrowser.open("[intra slot link]")--------> replce [intra slot link] with your intra slot link
    def open_github():
      	webbrowser.open("[github link]")------------> replace [github link] with your github link
</pre>
 <p>3. feel free to modify your own button</p>

<h2>Requirements for this program</h2>
 <p>- Available for window and mac user</p>
 <p>- python</p>
 <p>- pip</p>
 <p>- pyinstaller</p>

<h2>you have two option to install</h2>
<h3>OPTION 1</h3>

1. check your pyinstaller does it exist

        pyinstaller -v

2. if not exit try to install with pip

        pip install pyinstaller

3. compile the install.py

        python install.py

4. done (your exe file is in "dist" folder)

<h3>OPTION 2</h3>
<p>[ PYTHON FILE TO EXE FILE ]<p>

1. check your pyinstaller does it exist

        pyinstaller -v

2. if not exit try to install with pip

        pip install pyinstaller

3. (window: use power shell)now you can convert the python file to executable file
[ replace "pyinstaller.exe path" with the path you get (example: C:\Users\[YOUR_USER_NAME]\AppData\...Scripts\pyinstaller.exe) and "your_script_name.py" is the name of your python file ]

        python [pyinstaller.exe path] --onefile [your_script_name.py]

3. (macos) (replace "your_script_name.py" with the name of your python file)

        pyinstaller --onefile --windowed [your_script_name.py]

4. done (your exe file is in "dist" folder)

PS: the ui is very ugly hope you guys don't mind
