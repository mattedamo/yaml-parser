import os, yaml

#controlla se esiste
def create_patchesJson(ns_path):
    ns_path = "kustomize/overlay/prod/"
    kind_name = "sono_backend"
    tier = "backend"
    kustomize_path = ns_path + "kustomization.yaml"
    with open(kustomize_path) as file:
            kustomization = yaml.load(file, Loader=yaml.FullLoader)
    
    if "patches" not in kustomization.keys():
        entry["balla"][0] = [{"target": {"name" : "aa", "labelSelector" : "tier="}, "path" : "_patch.yaml"}]
        print(entry)
        #kustomization["patches"] = {[entry]}
       

    
create_patchesJson("")