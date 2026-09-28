import csv
import subprocess

targetFile = "file"

def read_csv(targetFile):
    with open(targetFile, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            rows.append(row)
        return rows

def send_to_c(rows):
    data = ""

    for row in rows:
        data += ",".join(row) + "\n"

    result = subprocess.run(
        ["translator.exe"],
        input=data,
        text=True,
        capture_output=True
    )

    print(result.stdout)

def main():
    running = True
    while running:
        targetFile = input("Type exit to end or Enter CSV filename: ")
        if targetFile == "exit":
            running = False
            break
        read_csv(targetFile)
        send_to_c(read_csv(targetFile))
        print("\nFinished reading CSV.")


if __name__ == "__main__":
    main()