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


## Notes from devs:

**Be aware that Pymake is by no means perfect, but it will improve.**

- Hopefully it works for your usecase!

### Q/A

- (Q) Why is the file size of the `.exe` files so big compared to `.py`?
(A) Because that's just how pyinstaller bundles the prerequisites and the Python interpreter, combined with the source code into a single file. Feel free to compress the executables using: https://upx.github.io/
- (Q) What licence is Pymake under?
(A) Pymake is licenced under the Apache 2.0 Licence (Details available on the LICENCE tab).
