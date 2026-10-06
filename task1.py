from pathlib import Path
import sys


NAME = "Illya"
SURNAME = "Vorobey"
GROUP = "IT-31"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    paths = sys.argv[1:]

    if not paths:
        print(
            "usage: python3 task1.py <path> [<path> ...]",
            file=sys.stderr
        )
        return 2

    checked = 0
    failed = 0

    for path_text in paths:
        checked += 1
        path = Path(path_text)

        try:
            if path.is_dir():
                raise IsADirectoryError(path_text)

            text = path.read_text(encoding="utf-8")

            lines = text.splitlines()

            if not lines:
                raise ValueError("file is empty")

            print(
                f"ok:    {path}: {len(lines)} lines, "
                f"first: {lines[0]}"
            )

        except FileNotFoundError:
            failed += 1
            print(
                f"error: {path}: file not found (FileNotFoundError)",
                file=sys.stderr
            )

        except IsADirectoryError:
            failed += 1
            print(
                f"error: {path}: is a directory (IsADirectoryError)",
                file=sys.stderr
            )

        except UnicodeDecodeError:
            failed += 1
            print(
                f"error: {path}: not a UTF-8 text file "
                f"(UnicodeDecodeError)",
                file=sys.stderr
            )

        except ValueError as error:
            failed += 1
            print(
                f"error: {path}: {error} (ValueError)",
                file=sys.stderr
            )

        except PermissionError:
            failed += 1
            print(
                f"error: {path}: permission denied (PermissionError)",
                file=sys.stderr
            )

    print(f"checked {checked}, failed {failed}")

    if failed:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
