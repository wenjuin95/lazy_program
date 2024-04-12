<h1>LAZY PROGRAM</h1>

![image](https://github.com/wenjuin95/lazy_program/blob/main/Untitled.png)

<p>1. i try to make a program that help me to open the website i always visit with button</p>
<p>2. if you want your own button you can go to custom.py to modified your self</p>

<h2>Available for window and mac user</h2>
<h2>Requirements for this program</h2>
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
<p>[ TURN PYTHON FILE TO EXE FILE ]<p>

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

