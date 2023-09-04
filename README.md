# Calculator App with Python and ttkbootstrap
This is a simple calculator application built using Python and the ttkbootstrap library. It provides basic arithmetic operations, percentage calculation, and modification options like clearing the display, changing sign, and adding decimal points.

![image](https://github.com/suibhne-sweeney/DesktopCalculatorProject/assets/110748326/ada678f2-b49f-49ea-9772-a889057d924a)


## Features
- Addition, subtraction, multiplication, and division operations.
- Percentage calculation.
- Clearing the display (CE) and the entire equation (C).
- Changing the sign of the current number (+/-).
- Adding decimal points.
- Accurate evaluation of mathematical expressions using the eval() function.
- User-friendly graphical user interface (GUI) with a modern and sleek design.

## Requirements
To run this calculator app, you need:

- Python 3.x installed on your system.
- The ttkbootstrap library for styling the application.

You can install ttkbootstrap using pip:


```
pip install ttkbootstrap
```

## Usage
1. Clone this repository to your local machine:
```
git clone https://github.com/your-username/calculator-app.git
```

2. Navigate to the project directory:
```
cd calculator-app
```

3. Run the calculator app:
```
python calculator.py
```
4. Start performing calculations with the user-friendly interface.

## How It Works
- The calculator app is implemented as a Python class (Calculator) that inherits from the ttk.Frame class.
- It uses the ttkbootstrap library for styling buttons and labels.
- The main components of the calculator are the display, numerical keypad, and event handlers for button clicks.
- Arithmetic operations are performed by constructing a mathematical expression as a string and then evaluating it using the eval() function.
- The app handles edge cases like changing the sign of a number, adding decimal points, and calculating percentages.

## Contributing
Contributions are welcome! If you'd like to improve this calculator app, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b feature-name.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to your branch: git push origin feature-name.
5. Create a pull request on GitHub.

## License
This calculator app is open-source and available under the MIT License.

## Acknowledgments
Thanks to the authors of the ttkbootstrap library for making it easy to create stylish GUI applications in Python.

## Support
If you find this project helpful, consider giving it a ⭐️ on GitHub. Your support is greatly appreciated!

Happy calculating! 🧮
