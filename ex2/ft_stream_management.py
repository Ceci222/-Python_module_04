import sys
import typing


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    print()
    sys.exit(1)
else:
    file = sys.argv[1]


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
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
        print(f"[STDERR] Error opening file '{file}': {e}", file=sys.stderr)
        print()
        sys.exit(1)

    try:
        print("Enter new file name (or empty): ", end="", flush=True)
        #  end avoids '\n' so it prints and receoves on same line
        # flush=True -> forces the print before the next '\n'
        new_file_name = sys.stdin.readline().rstrip("\n")

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
        print(f"[STDERR] Error opening file '{new_file_name}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        print()


if __name__ == "__main__":
    main()
