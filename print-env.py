import os


def main():
    print(os.environ)
    print(os.getenv("NS"))
    print(os.getenv("STOPPIN"))
if __name__ == '__main__':
    main()
