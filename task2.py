from pathlib import Path
import sys


NAME = "Illya"
SURNAME = "Vorobey"
GROUP = "IT-31"


def usage():
    print(
        "usage: python3 task2.py [--force] <source> <destination>",
        file=sys.stderr
    )


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]
    force = False

    if args and args[0] == "--force":
        force = True
        args = args[1:]

    if len(args) != 2:
        usage()
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        if not source.exists():
            raise FileNotFoundError

        if source.is_dir():
            raise IsADirectoryError

        if destination.exists() and destination.is_dir():
            raise IsADirectoryError

        if destination.exists():
            try:
                if source.samefile(destination):
                    print(
                        "error: source and destination are the same file",
                        file=sys.stderr
                    )
                    return 1
            except OSError:
                pass

            if not force:
                print(
                    f"error: {destination} already exists, "
                    f"use --force to overwrite",
                    file=sys.stderr
                )
                return 1

        parent = destination.parent

        if not parent.exists():
            print(
                f"error: destination folder {parent} not found",
                file=sys.stderr
            )
            return 1

        if not parent.is_dir():
            print(
                f"error: destination folder {parent} is not a directory",
                file=sys.stderr
            )
            return 1

        # Читаємо джерело як UTF-8 текст до початку запису.
        # Якщо файл не текстовий, destination не буде пошкоджено.
        content = source.read_text(encoding="utf-8")

        destination.write_text(content, encoding="utf-8")

        print(f"copied: {source} -> {destination}")
        return 0

    except FileNotFoundError:
        print(
            f"error: source {source} not found",
            file=sys.stderr
        )
        return 1

    except IsADirectoryError:
        if source.is_dir():
            print(
                f"error: source {source} is a directory, not a file",
                file=sys.stderr
            )
        else:
            print(
                f"error: destination {destination} is a directory, "
                f"not a file",
                file=sys.stderr
            )
        return 1

    except UnicodeDecodeError:
        print(
            f"error: source {source} is not a UTF-8 text file",
            file=sys.stderr
        )
        return 1

    except PermissionError:
        print(
            "error: permission denied",
            file=sys.stderr
        )
        return 1

    except OSError as error:
        print(
            f"error: cannot copy file: {error}",
            file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
