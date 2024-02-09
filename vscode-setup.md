# Python Development Environment Setup in Visual Studio Code

## Prerequisites

1. Install [Python](https://www.python.org/downloads/) on your machine.
2. Install [Visual Studio Code](https://code.visualstudio.com/download) on your machine.

## Steps to Setup Visual Studio Code for Python

1. Open Visual Studio Code.

2. Go to the Extensions view (`View` -> `Extensions`).

3. In the Extensions view, search for `Python`. Find the Python extension by Microsoft and click on the Install button.

4. After the Python extension is installed, open the Command Palette (`View` -> `Command Palette` or `Ctrl+Shift+P`).

5. In the Command Palette, type `Python: Select Interpreter` and select it.

6. A list of available Python interpreters is displayed. Select the Python interpreter you want to use.

7. Now, you can create a new Python file (`File` -> `New File`) and save it with the `.py` extension.

8. To run the Python file, right-click anywhere in the file and select `Run Python File in Terminal`.

## Debugging Python in Visual Studio Code

1. Open the Python file you want to debug.

2. Go to the Run view (`View` -> `Run`).

3. Click on the `create a launch.json file` link.

4. In the dropdown, select `Python File`.

5. A `launch.json` file is created in a `.vscode` folder in your workspace which allows you to configure your debugging settings.

6. To start debugging, select `Run` -> `Start Debugging` or press `F5`.

For more detailed instructions, refer to the [Python tutorial in Visual Studio Code documentation](https://code.visualstudio.com/docs/python/python-tutorial).