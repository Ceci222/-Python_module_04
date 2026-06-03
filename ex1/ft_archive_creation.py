import sys
import typing


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    print()
    sys.exit(1)
else:
    file = sys.argv[1]


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file}'")

    try:
        f: typing.IO = open(file, 'r')

        print("---")
        print()

        content = f.read()
        print(content)

        print()
        print("---")

        f.close()
        print(f"File '{file}' closed.")
        print()

        print("Transform data:")
        print("---")
        print()
        modified_lines = [line + "#" for line in content.splitlines()]

        for line in modified_lines:
            print(line)

        print()
        print("---")
    except OSError as e:
        print(f"Error opening file '{file}': {e}")
        print()

    try:
        new_file_name = input("Enter new file name (or empty): ")

        if new_file_name == "":
            print("Not saving data.")
            sys.exit()
        else:
            print(f"Saving data to '{new_file_name}'")
            f = open(new_file_name, 'w')  # no typehint here or mypy complains
            text_to_save = "\n".join(modified_lines) + "\n"
            f.write(text_to_save)  # this saves the content
            print(f"Data saved in file '{new_file_name}'.")
            print()
            f.close()
    except OSError as e:
        print(f"Error opening file '{file}': {e}")
        print()


if __name__ == "__main__":
    main()
