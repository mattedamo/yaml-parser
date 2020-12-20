import yaml
#in the first version of the yaml customization
#here I update only deployment file
#and only number of replicas
#how to identify the correct file and namespace?
#I specify the name in metadata
#I specify the namespace in the namespace metadata
def main():
    with open("./file.yaml") as file:
        file_yaml = yaml.load(file, Loader=yaml.FullLoader)
        print(file_yaml)
        
#    for element in file_yaml:
#        print(element)
    if file_yaml["replicas"]:
        print(file_yaml["replicas"])
    if file_yaml["spec"]["caster"]["master"]["name"]:
        print(file_yaml["spec"]["caster"]["master"]["name"][0]["name"])




if __name__ == '__main__':
    main()