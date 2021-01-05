import yaml

def main():
    with open("./test.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    #print(input)
    #prima controllo quale è il namespace e lo rimuovo siccome non mi serve più

    for k,v in input.items():
        if k == "backend":
            be = v

        if k == "frontend":
            fe = v

    print(be)
    for x in be:
        if(x["type"] == "deployment"):
            x.pop("type")
            deployment = x

        elif(x["type"] == "service"):
            x.pop("type")
            service = x
    
    print(service)
    print(deployment)

    #le variabili sono pronte, adesso voglio editare i target yamls
    if deployment != None:
        for k,v in deployment.items():
            if(k == "replicas"):
                replicas = v
    
    print(replicas)

    with open("./kustomize/base/deployment-backend.yaml") as file:
        output = yaml.load(file, Loader=yaml.FullLoader)
    print(output)
    output["spec"]["replicas"] = 19
    
    print(output)
    
    with open("./kustomize/base/deployment-backend.yaml", 'w') as file:
        yaml.dump(output, file)

if __name__ == '__main__':
    main()