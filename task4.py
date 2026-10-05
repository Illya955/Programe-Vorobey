from pathlib import Path
import sys


def analyze_directory(directory):
    directory = Path(directory).expanduser().resolve()

    if not directory.exists():
        print(f"error: directory does not exist: {directory}")
        return

    if not directory.is_dir():
        print(f"error: not a directory: {directory}")
        return

    files = [
        path for path in directory.rglob("*")
        if path.is_file()
    ]

    print(f"directory: {directory}")
    print(f"files found: {len(files)}")
    print()

    if not files:
        print("No files found.")
        return

    total_size = 0

    for path in files:
        try:
            size = path.stat().st_size
            total_size += size
            print(
                f"{path.relative_to(directory)} "
                f"- {size} bytes"
            )
        except OSError:
            print(
                f"{path.relative_to(directory)} "
                f"- unable to read"
            )

    print()
    print(f"total size: {total_size} bytes")


def main():
    if len(sys.argv) < 2:
        print("usage: python task4.py <directory>")
        print("example: python task4.py ~/Downloads")
        return

    analyze_directory(sys.argv[1])


if __name__ == "__main__":
    main()
