from pathlib import Path
from collections import defaultdict
from datetime import datetime
import sys


NAME = "Illya"
SURNAME = "Vorobey"
GROUP = "IT-31"
BIRTH_DAY = 5


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

EXPENSES_FILE = DATA_DIR / "expenses.csv"
REPORT_FILE = REPORTS_DIR / "expenses_report.txt"


def usage():
    print(
        "usage: python3 task3.py add <date> <category> <amount> <note>",
        file=sys.stderr
    )
    print(
        "       python3 task3.py list",
        file=sys.stderr
    )
    print(
        "       python3 task3.py report",
        file=sys.stderr
    )


def validate_record(date_text, category, amount_text, note):
    """
    Єдина перевірка запису.
    Використовується і під час add, і під час читання CSV.
    """

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"bad date '{date_text}'")

    try:
        amount = float(amount_text)
    except ValueError:
        raise ValueError(f"bad amount '{amount_text}'")

    if amount <= 0:
        raise ValueError(
            f"amount must be positive, got {amount_text}"
        )

    if not category:
        raise ValueError("category must not be empty")

    if not note:
        raise ValueError("note must not be empty")

    return {
        "date": date_text,
        "category": category,
        "amount": amount,
        "note": note,
    }


def read_expenses():
    """
    Єдине місце для перевірки самого файлу та читання його записів.

    Повертає:
        expenses — коректні записи;
        skipped — список (номер рядка, причина).
    """

    if not EXPENSES_FILE.exists():
        raise FileNotFoundError

    if EXPENSES_FILE.is_dir():
        raise IsADirectoryError

    try:
        text = EXPENSES_FILE.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise

    expenses = []
    skipped = []

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        if len(parts) != 4:
            skipped.append(
                (
                    line_number,
                    f"expected 4 fields, got {len(parts)}"
                )
            )
            continue

        date_text, category, amount_text, note = parts

        try:
            expense = validate_record(
                date_text,
                category,
                amount_text,
                note
            )
        except ValueError as error:
            skipped.append((line_number, str(error)))
            continue

        expenses.append(expense)

    return expenses, skipped


def print_skipped(skipped):
    if not skipped:
        return

    print(
        f"skipped {len(skipped)} bad line(s):",
        file=sys.stderr
    )

    for line_number, reason in skipped:
        print(
            f"  line {line_number}: {reason}",
            file=sys.stderr
        )


def handle_file_error():
    try:
        # Перевірка виконується централізовано через read_expenses().
        return read_expenses()
    except FileNotFoundError:
        print(
            f"error: {EXPENSES_FILE} not found",
            file=sys.stderr
        )
    except IsADirectoryError:
        print(
            f"error: {EXPENSES_FILE} is a directory, not a file",
            file=sys.stderr
        )
    except UnicodeDecodeError:
        print(
            f"error: {EXPENSES_FILE} is not a UTF-8 text file",
            file=sys.stderr
        )
    except PermissionError:
        print(
            f"error: cannot read {EXPENSES_FILE}: permission denied",
            file=sys.stderr
        )
    except OSError as error:
        print(
            f"error: cannot read {EXPENSES_FILE}: {error}",
            file=sys.stderr
        )

    return None


def add_expense(args):
    if len(args) < 4:
        print(
            "error: add needs date, category, amount and note",
            file=sys.stderr
        )
        usage()
        return 2

    date_text = args[0]
    category = args[1]
    amount_text = args[2]
    note = " ".join(args[3:])

    # Спочатку перевіряємо сам запис.
    try:
        expense = validate_record(
            date_text,
            category,
            amount_text,
            note
        )
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1

    # Перед записом перевіряємо файл.
    result = handle_file_error()

    if result is None:
        print("nothing was added", file=sys.stderr)
        return 1

    try:
        with EXPENSES_FILE.open("a", encoding="utf-8") as file:
            file.write(
                f"{expense['date']};"
                f"{expense['category']};"
                f"{expense['amount']:.2f};"
                f"{expense['note']}\n"
            )
    except OSError as error:
        print(
            f"error: cannot write {EXPENSES_FILE}: {error}",
            file=sys.stderr
        )
        print("nothing was added", file=sys.stderr)
        return 1

    print(
        f"added: {expense['date']} "
        f"{expense['category']} "
        f"{expense['amount']:.2f} "
        f"({expense['note']})"
    )

    return 0


def list_expenses():
    result = handle_file_error()

    if result is None:
        return 1

    expenses, skipped = result

    if not expenses:
        print("no expenses found")
        print_skipped(skipped)
        return 0

    print(
        f"{'date':<12}"
        f"{'category':<15}"
        f"{'amount':>8}  "
        f"note"
    )

    for expense in expenses:
        print(
            f"{expense['date']:<12}"
            f"{expense['category']:<15}"
            f"{expense['amount']:>8.2f}  "
            f"{expense['note']}"
        )

    total = sum(expense["amount"] for expense in expenses)

    print()
    print(f"{len(expenses)} records, total {total:.2f}")

    print_skipped(skipped)

    return 0


def build_report():
    result = handle_file_error()

    if result is None:
        return 1

    expenses, skipped = result

    if not expenses:
        print(
            "error: nothing to report, no valid records",
            file=sys.stderr
        )
        print_skipped(skipped)
        return 1

    total = sum(expense["amount"] for expense in expenses)

    dates = [expense["date"] for expense in expenses]
    first_date = min(dates)
    last_date = max(dates)

    categories = defaultdict(
        lambda: {"count": 0, "total": 0.0}
    )

    for expense in expenses:
        category = expense["category"]
        categories[category]["count"] += 1
        categories[category]["total"] += expense["amount"]

    category_rows = []

    for category, data in categories.items():
        share = data["total"] / total * 100
        chart = "#" * int(share / 5)

        category_rows.append(
            (
                category,
                data["count"],
                data["total"],
                share,
                chart
            )
        )

    category_rows.sort(
        key=lambda row: row[2],
        reverse=True
    )

    days = defaultdict(float)

    for expense in expenses:
        days[expense["date"]] += expense["amount"]

    top_day = max(
        days.items(),
        key=lambda item: item[1]
    )

    most_expensive = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    number_of_days = len(days)
    average_per_day = total / number_of_days

    lines = []

    lines.append(
        f"Expenses report for {NAME} {SURNAME} ({GROUP})"
    )
    lines.append(
        f"Period: {first_date} .. {last_date}"
    )
    lines.append(
        f"Records: {len(expenses)}"
    )
    lines.append("")

    lines.append(
        f"{'category':<12}"
        f"{'count':>6}"
        f"{'total':>11}"
        f"{'share':>8}  "
        f"chart"
    )

    lines.append("-" * 52)

    for category, count, category_total, share, chart in category_rows:
        lines.append(
            f"{category:<12}"
            f"{count:>6}"
            f"{category_total:>11.2f}"
            f"{share:>7.1f}%  "
            f"{chart}"
        )

    lines.append("-" * 52)

    lines.append(
        f"{'total':<12}"
        f"{len(expenses):>6}"
        f"{total:>11.2f}"
        f"{100.0:>7.1f}%"
    )

    lines.append("")

    lines.append(
        f"Top day: {top_day[0]} ({top_day[1]:.2f})"
    )

    lines.append(
        f"Most expensive: "
        f"{most_expensive['category']} "
        f"{most_expensive['amount']:.2f} "
        f"({most_expensive['note']})"
    )

    lines.append(
        f"Average per day: {average_per_day:.2f}"
    )

    report = "\n".join(lines)

    try:
        REPORTS_DIR.mkdir(exist_ok=True)

        REPORT_FILE.write_text(
            report + "\n",
            encoding="utf-8"
        )
    except OSError as error:
        print(
            f"error: cannot save report: {error}",
            file=sys.stderr
        )
        return 1

    print(report)
    print()
    print(f"report saved to: {REPORT_FILE}")

    print_skipped(skipped)

    return 0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]

    if not args:
        usage()
        return 2

    command = args[0]

    if command == "add":
        return add_expense(args[1:])

    if command == "list":
        if len(args) != 1:
            usage()
            return 2
        return list_expenses()

    if command == "report":
        if len(args) != 1:
            usage()
            return 2
        return build_report()

    print(
        f"error: unknown command {command}",
        file=sys.stderr
    )
    usage()
    return 2


if __name__ == "__main__":
    sys.exit(main())
