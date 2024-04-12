<h1>LAZY PROGRAM</h1>

<p>1. i try to make a program that help me to open website with button</p>
<p>2. if you want your own button you can go to custom.py to modified your self</p>

<h2>TURN PYTHON FILE TO EXE FILE GUIDE</h2>

1. check your pyinstaller does it exist

        pyinstaller -v

2. if not exit try to install with pip

        pip install pyinstaller

3. (window: use power shell)now you can convert the python file to executable file
[ replace "pyinstaller.exe path" with the path you get (example: C:\Users\[YOUR_USER_NAME]\AppData\...Scripts\pyinstaller.exe) and "your_script_name.py" is the name of your python file ]

        python [pyinstaller.exe path] --onefile [your_script_name.py]

3. (macos) (replace "your_script_name.py" with the name of your python file)

        pyinstaller --onefile --windowed [your_script_name.py]

4. it will generate the exe file to the dist folder.

<h2>Available for window and mac user</h2>
