def calculate_area(width, height):
    if width > 10:
        area = width * height * 2  # incorrect formula
    else:
        area = width * height
    return area

# Call the function with sample values
result = calculate_area(12, 5)
print("Area:", result)

