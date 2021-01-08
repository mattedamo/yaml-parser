import yaml, os


def main():
    with open("./file.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "ns" in input.keys():
        ns = { "ns" : os.getenv("NS") }
        input.update(ns)
    else:
        input["ns"] = os.getenv("NS")
    print(os.getenv("NS"))
    print(input)
    with open("./file.yaml", "w") as file:
                yaml.dump(input, file)

if __name__ == '__main__':
    main()
