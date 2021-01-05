import yaml
from yaml_update import yaml_updates
from kind_name import getKindName

def main():
    with open("./file.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    #print(input)
    #prima controllo quale è il namespace e lo rimuovo siccome non mi serve più

    if "ns" not in input:
        raise Exception("missing ns")
    else:
        ns_path = "kustomize/overlay/"+input['ns']
        input.pop('ns')
    #print(ns_path)


    be = None
    fe = None
    db = None

    for k,v in input.items():
        if k == "backend":
            be = v
        elif k == "frontend":
            fe = v
        elif k == "db":
            db = v
    
    if be != None:
        kind_name = getKindName("backend")
        #print(kind_name)
        yaml_updates(be, ns_path, kind_name, "backend")


    """
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
        """

if __name__ == '__main__':
    main()