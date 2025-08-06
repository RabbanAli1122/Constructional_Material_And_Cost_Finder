def get_float(prompt):
    return float(input(f"\n{prompt}\n> "))

def get_int(prompt):
    return int(input(f"\n{prompt}\n> "))

def get_choice(prompt, choices):
    print(f"\n{prompt}")
    for k, v in choices.items():
        print(f"{k}: {v}")
    return int(input("\nEnter your choice: "))

def unit_conversion(unit):
    conversions = {
        1: 12,          # feet to inches
        2: 39.3701,     # meters to inches
        3: 1,           # inches
        4: 0.393701,    # cm to inches
        5: 0.0393701    # mm to inches
    }
    return conversions.get(unit, 1)

def wall_calculation():
    brick_length = get_float("Enter the brick length (in inches):")
    brick_width = get_float("Enter the brick width (in inches):")
    unit = get_choice("Select wall measurement unit:", {
        1: "Feet",
        2: "Meters",
        3: "Inches",
        4: "Centimeters",
        5: "Millimeters"
    })

    length = get_float(f"Enter wall width (in selected unit):")
    height = get_float(f"Enter wall height (in selected unit):")
    base = input("Does the wall include a base? (yes/no): ").strip().lower() == 'yes'

    if base:
        base_unit = get_choice("Select base wall height unit:", {
            1: "Feet",
            2: "Meters",
            3: "Inches",
            4: "Centimeters",
            5: "Millimeters"
        })
        base_height = get_float("Enter the height of base wall (in selected unit):")
        base_factor = unit_conversion(base_unit)
        base_height_inches = base_height * base_factor
    else:
        base_height_inches = 0

    factor = unit_conversion(unit)
    length_in_inches = length * factor
    height_in_inches = height * factor

    horizontal = length_in_inches / brick_length + base_height_inches
    vertical = height_in_inches / brick_width
    bricks = round(horizontal * vertical, 2)
    cement_bags = round((3.5 / 1000) * bricks, 2)
    sand_cuft = round((30 / 1000) * bricks, 2)

    print("\n--- Wall Material Estimation ---")
    print(f"Bricks Required: {bricks}")
    print(f"Cement Required: {cement_bags} bags")
    print(f"Sand Required: {sand_cuft} cubic feet")

def plaster_calculation():
    unit = get_choice("Select wall measurement unit:", {
        1: "Feet",
        2: "Meters",
        3: "Inches",
        4: "Centimeters",
        5: "Millimeters"
    })

    length = get_float("Enter wall width (in selected unit):")
    height = get_float("Enter wall height (in selected unit):")
    thickness_mm = get_float("Enter plaster thickness (in millimeters):")

    # Convert units to meters
    length_m = length / 3.28 if unit == 1 else length
    height_m = height / 3.28 if unit == 1 else height
    if unit == 2:
        pass
    elif unit == 3:
        length_m = length * 0.0254
        height_m = height * 0.0254
    elif unit == 4:
        length_m = length * 0.01
        height_m = height * 0.01
    elif unit == 5:
        length_m = length * 0.001
        height_m = height * 0.001

    thickness_m = thickness_mm / 1000
    volume = length_m * height_m * thickness_m * 1.27
    cement = round((volume * (1/5)) / 0.035 - 0.1, 2)
    sand = round((volume * (4/5)) * 35.3 - 0.3)

    print("\n--- Plaster Material Estimation ---")
    print(f"Cement Required: {cement} bags")
    print(f"Sand Required: {sand} cubic feet")

def main():
    while True:
        try:
            print("\n--- Construction Material Calculator ---")
            option = get_choice("Select the operation:", {
                0: "Exit",
                1: "Brick, Cement, Cost and Sand for a Wall",
                2: "Cement and Sand for Plastering a Wall"
                
            })

            if option == 1:
                wall_calculation()
            elif option == 2:
                plaster_calculation()
            elif option == 0:
                print("\nExiting the program. Goodbye!")
                exit(0)
            else:
                print("Invalid Option!")

            again = input("\nEnter 0 to Exit, or 1 to Return to Menu:\n> ").strip()
            if again == '0':
                print("\nExiting the program. Goodbye!")
                exit(0)

        except Exception as e:
            print(f"\n❌ Something went wrong: {e}")
            print("Restarting the program...\n")

if __name__ == "__main__":
    main()
