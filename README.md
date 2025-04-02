# Pymake - The Ultimate WebAPP maker for your needs.


Prerequisites

- ```pip install PyQt6 PyQt6-WebEngine pyinstaller``` |For 1.0 Full Release onwards.

  **Or** run the included batch script (If you are on Windows).

-------------------------------------------------------------------------------------

- ```pip install PyQt5 PyQtWebEngine pyinstaller```  |For 1.0 Pre-Release (Legacy)


---
# Usage

1) Run Pymake ```python Pymake.py```
2) Enter the app name and the URL of the website you want to convert to a Web Application.
3) When prompted to build the executable, type Y (if you want to get a .exe file).
4) Navigate to the `webapps` folder inside your build directory to access your freshly built app.

**Pymake is provided in both .py and .exe forms.**


  ### Your FileTree should look like this:

![image](https://github.com/user-attachments/assets/fe73d65f-c396-4dbd-8fe8-583ce22b624d)

  In the `webapps` folder theres a `.py` file of the generated script (which contains the source code) and a `.exe` file (if you chose to generate one).

![image](https://github.com/user-attachments/assets/cc07e8e1-737a-42fa-9dfc-11d915d8829f)

-------------------------------------------------------------------------------------
## How does the app look like?
1. **Upon launching Pymake, you are greeted with this:**

![image](https://github.com/user-attachments/assets/f8671afe-73be-446c-bea5-a583331e0277)

At this stage you are told to enter a name and URL for the webapp you want to create. Rest is self explanatory.

2. **Upon inputting name and URL, the .py script is generated and saved in the `webapps` folder.**

![image](https://github.com/user-attachments/assets/45502de9-b351-42fc-82a5-278e02482405)

You are now asked wether you wish to build an executable or not. The build process utilizes `pyinstaller` and generates a relatively large file (~155MB).
- We only recommend building the executable if you want portability and/or running it on computers that do not have python installed.

## Notes from devs:

**Be aware that Pymake is by no means perfect, but it will improve.**

- Hopefully it works for your usecase!

### Q/A

- (Q) Why are .exe files significantly larger than .py files?

(A) This is because PyInstaller bundles the Python interpreter, dependencies, and source code into a single executable file. You can reduce the file size by compressing the executable using: https://upx.github.io/


- (Q) What licence is Pymake under?

(A) Pymake is licenced under the Apache 2.0 Licence (Details available on the LICENCE tab).
