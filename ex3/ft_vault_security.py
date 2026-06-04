
#  only the firstst param is obligatory
def secure_archive(filename: str, action: str ="read" , content: str ="") -> tuple[bool, str]:
    try:
        if action == 'read':
            with open(filename, "r") as f:
                content = f.read()
            return (True, content)
        elif action == 'write':
            with open(filename, "w") as f:
                f.write(content) #it starts as an empty string
                content = 'Content successfully written to file'      
            return (True, content)
        else:
            return (False, "Unknown action")

    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    # etc/shadow for linux
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", result[1]))
    # content[1] -> only reads2nd element of the tuple --> True, content
    print()

if __name__ == "__main__":
    main()