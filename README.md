# 🧱 Construction Material Calculator

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A Python-based terminal program to calculate required **bricks, cement, and sand** for constructing or plastering walls. The tool supports **multiple unit conversions** for user convenience and includes error handling for a seamless experience.

## ✅ Features

- Calculate materials for:
  - Brick wall construction
  - Wall plastering
- Supports unit input in:
  - Feet
  - Meters
  - Inches
  - Centimeters
  - Millimeters
- Optional wall base calculation
- Converts all measurements to standard units internally
- Clean, interactive CLI interface
- Built-in exception handling and looped menu system


## 📦 How It Works

### 🧱 Wall Construction Estimator

1. User inputs brick size in inches.
2. Select wall dimensions and input units.
3. Enter wall height and width.
4. Optionally enter base wall height and units.
5. Get required:
   - Number of bricks
   - Bags of cement
   - Cubic feet of sand

### 🧱 Wall Plaster Estimator

1. Select units for wall dimensions.
2. Enter wall height and width.
3. Enter plaster thickness (in mm).
4. Get required:
   - Bags of cement
   - Cubic feet of sand


## 🖥️ Demo

```bash
$ python construction_calculator.py

--- Construction Material Calculator ---
1: Brick, Cement, Cost and Sand for a Wall
2: Cement and Sand for Plastering a Wall
0: Exit
> 1

Enter the brick length (in inches):
> 9

Enter the brick width (in inches):
> 4.5

Select wall measurement unit:
1: Feet
2: Meters
...
> 1

Enter wall width (in selected unit):
> 12

Enter wall height (in selected unit):
> 10

Does the wall include a base? (yes/no):
> no

--- Wall Material Estimation ---
Bricks Required: 3840.0
Cement Required: 13.44 bags
Sand Required: 115.2 cubic feet
```


## 🛠️ Technologies Used
1. Python 3
2. CLI (Command Line Interface)
3. Exception Handling
4. Custom Unit Conversion
5. Simple Math and Volume Calculations

## 📄 File Structure
construction_calculator.py  # Main Python script
README.md                   # Documentation


## 🚀 Getting Started
### Prerequisites
- Python 3.x installed on your system

### Run the Program
```
python construction_calculator.py
```

## 🤖 Functions Overview

- 🔢 **get_float()** – Handles float input from the user
- 🔢 **get_int()** – Handles integer input
- 🔘 **get_choice()** – Displays multiple choices and fetches the user’s selection
- 📏 **unit_conversion()** – Converts selected input units to inches (for consistent internal calculations)
- 🧱 **wall_calculation()** – Calculates the number of bricks, cement bags, and sand required for wall construction
- 🎨 **plaster_calculation()** – Calculates the volume and required materials for wall plastering
- 🚀 **main()** – Displays the menu, handles user options, loops, and manages all errors gracefully


## 🙏 Acknowledgements
Thanks to Python and its simplicity in building such practical tools for construction estimations.

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
