from tablestats import *


def main():
    with open(input(), encoding="utf-8") as table:
        rows = read_rows(table)
        
    count = count_types(rows)
    print(len(rows))
    print(len(count))
    print(total_minutes(rows, "ошибка"))

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(count))


if __name__ == "__main__":
    main()
