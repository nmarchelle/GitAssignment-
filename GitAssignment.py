def rect_area(length, width):
    """Compute the area of a rectangle."""
    return length * width


def rect_surface_area(length, width, height):
    """Compute the surface area of a rectangular solid."""
    base_area = rect_area(length, width)
    side_area1 = rect_area(length, height)
    side_area2 = rect_area(width, height)
    return 2 * (base_area + side_area1 + side_area2)


def main():
    # Input length, width, and height from the user
    length = int(input("Enter the length of the rectangular solid: "))
    width = int(input("Enter the width of the rectangular solid: "))
    height = int(input("Enter the height of the rectangular solid: "))

    # Compute surface area using rect_surface_area function
    surface_area = rect_surface_area(length, width, height)

    # Print input values and surface area
    print("\nLength:", length)
    print("Width:", width)
    print("Height:", height)
    print("Surface Area:", surface_area)


# Call the main function
if __name__ == "__main__":
    main()
