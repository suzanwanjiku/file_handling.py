def process_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open("new_file.txt", "w") as outfile:
            outfile.write(modified_content)

        print("Success! Modified file saved as 'new_file.txt'")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

process_file()
