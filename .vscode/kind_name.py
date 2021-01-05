import os, yaml

def getKindName(tierValue):
    tierValue = tierValue
    kind_name = {}
    for filename in os.listdir("kustomize/base/"):
        with open(os.path.join("kustomize/base/", filename)) as file:
            input = yaml.load(file, Loader=yaml.FullLoader)
        if input["kind"] == "Deployment":
            if input["spec"]["template"]["metadata"]["labels"]["tier"] == tierValue:
                kind_name["deployment"] = input["metadata"]["name"]
        elif input["kind"] == "Service":
            if input["spec"]["selector"]["tier"] == tierValue:
                kind_name["service"] = input["metadata"]["name"]
    return kind_name



