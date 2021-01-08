import yaml, os


def main():
    with open("./file.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    #prima controllo quale è il namespace e lo rimuovo siccome non mi serve più
    print(os.environ)
    input["ns"] = os.getenv("NS")
    with open("./file", "w") as file:
                yaml.dump(input, file)

if __name__ == '__main__':
    main()