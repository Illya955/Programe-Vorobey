from pathlib import Path
from collections import defaultdict
import sys


NAME = "Illya"
SURNAME = "Vorobey"
GROUP = "IT-31"


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

EXPENSES_FILE = DATA_DIR / "expenses.csv"
REPORT_FILE = REPORTS_DIR / "expenses_report.txt"


def usage():
    print("usage: python task3.py add <date> <category> <amount> <note>")
    print("       python task3.py list")
    print("       python task3.py report")


def ensure_file():
    DATA_DIR.mkdir(exist_ok=True)

    if not EXPENSES_FILE.exists():
        EXPENSES_FILE.write_text(
            "# date;category;amount;note\n",
            encoding="utf-8"
        )


def add_expense(args):
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        usage()
        return

    date = args[0]
    category = args[1]

    try:
        amount = float(args[2])
    except ValueError:
        print("error: amount must be a number")
        return

    note = " ".join(args[3:])

    ensure_file()

    with EXPENSES_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date};{category};{amount:.2f};{note}\n")

    print(f"added: {date} {category} {amount:.2f} ({note})")


def read_expenses():
    if not EXPENSES_FILE.exists():
        return []

    expenses = []

    with EXPENSES_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";")

            if len(parts) != 4:
                continue

            date, category, amount_text, note = parts

            try:
                amount = float(amount_text)
            except ValueError:
                continue

            expenses.append({
                "date": date,
                "category": category,
                "amount": amount,
                "note": note
            })

    return expenses


def list_expenses():
    expenses = read_expenses()

    if not expenses:
        print("no expenses found")
        return

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


def build_report():
    expenses = read_expenses()

    if not expenses:
        print("no expenses found")
        return

    total = sum(expense["amount"] for expense in expenses)

    dates = [expense["date"] for expense in expenses]
    first_date = min(dates)
    last_date = max(dates)

    categories = defaultdict(lambda: {"count": 0, "total": 0.0})

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

    category_rows.sort(key=lambda row: row[2], reverse=True)

    days = defaultdict(float)

    for expense in expenses:
        days[expense["date"]] += expense["amount"]

    top_day = max(days.items(), key=lambda item: item[1])

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

    REPORTS_DIR.mkdir(exist_ok=True)

    REPORT_FILE.write_text(
        report + "\n",
        encoding="utf-8"
    )

    print(report)
    print()
    print(f"report saved to: {REPORT_FILE}")


def main():
    args = sys.argv[1:]

    if not args:
        usage()
        return

    command = args[0]

    if command == "add":
        add_expense(args[1:])
    elif command == "list":
        list_expenses()
    elif command == "report":
        build_report()
    else:
        print(f"error: unknown command {command}")
        usage()


if __name__ == "__main__":
    main()
