from pathlib import Path


NAME = "Illya"
SURNAME = "Vorobey"
GROUP = "IT-31"
YEAR = 2008
LANGUAGE = "Python"


def show_project_tree(root):
    print("project tree:")

    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        indent = "  " * (len(relative.parts) - 1)

        if path.is_dir():
            print(f"{indent}{path.name}/")
        else:
            print(f"{indent}{path.name}")


def main():
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent
    cwd = Path.cwd()
    home = Path.home()

    print(f"cwd:         {cwd}")
    print(f"script:      {script_path}")
    print(f"script dir:  {script_dir}")
    print(f"home:        {home}")
    print()

    data_dir = script_dir / "data"
    reports_dir = script_dir / "reports"
    backups_dir = script_dir / "backups"

    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    backups_dir.mkdir(exist_ok=True)

    profile_path = data_dir / "profile.txt"

    profile_data = [
        f"name: {NAME}",
        f"surname: {SURNAME}",
        f"group: {GROUP}",
        f"year: {YEAR}",
        f"language: {LANGUAGE}",
    ]

    profile_path.write_text(
        "\n".join(profile_data) + "\n",
        encoding="utf-8"
    )

    print(f"profile path: {profile_path}")
    print(f"relative:     {profile_path.relative_to(script_dir)}")
    print(f"name:         {profile_path.name}")
    print(f"stem:         {profile_path.stem}")
    print(f"suffix:       {profile_path.suffix}")
    print(f"parent:       {profile_path.parent.name}")
    print(f"size:         {profile_path.stat().st_size} bytes")
    print()

    show_project_tree(script_dir)


if __name__ == "__main__":
    main()
