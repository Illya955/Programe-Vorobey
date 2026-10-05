from pathlib import Path
from datetime import datetime


NAME = "Illya"
SURNAME = "Vorobey"


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def add_run(path, number):
    path.parent.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};{NAME} {SURNAME}\n")


def show_history(path, last=3):
    if not path.exists():
        print("runs so far: 0")
        return

    records = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(";", 2)

            if len(parts) == 3:
                records.append(parts)

    print(f"runs so far: {len(records)}")
    print("last runs:")

    for number, stamp, name in records[-last:]:
        print(f"  #{number}  {stamp}  {name}")

    if records:
        print(f"first run was at {records[0][1]}")


def main():
    script_dir = Path(__file__).resolve().parent
    runs_path = script_dir / "data" / "runs.log"

    previous_runs = count_runs(runs_path)
    current_run = previous_runs + 1

    add_run(runs_path, current_run)

    if current_run == 1:
        print("runs.log was just created.")

    print(f"Hello, {NAME} {SURNAME}! This is run number {current_run}.")

    show_history(runs_path)


if __name__ == "__main__":
    main()
