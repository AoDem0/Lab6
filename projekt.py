import sys

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    file1, file2 = parse_args()
    print(f"File1: {file1}, File2: {file2}")