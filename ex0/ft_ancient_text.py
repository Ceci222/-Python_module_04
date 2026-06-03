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

    except OSError as e:
        print(f"Error opening file '{file}': {e}")
        print()


if __name__ == "__main__":
    main()
