COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Bright Lilac": "#d891ef",
    "Blue": "#0000ff",
    "BlueViolet": "#8a2be2",
    "Black": "#000000"
}

def get_color_hex(color_name):
    """
    Look up hexadecimal colour codes.
    """
    return COLOR_TO_HEX.get(color_name.capitalize(), "Invalid color name")


while True:
    color_input = input("Enter a color name (or just hit enter to stop): ").strip()
    if not color_input:
        break
    hex_code = get_color_hex(color_input)
    print(f"The hexadecimal code for {color_input} is {hex_code}")