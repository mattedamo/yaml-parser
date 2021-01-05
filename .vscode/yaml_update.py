import yaml, os

def yaml_updates(be, ns_path, kind_name, tier):
    tier = tier
    for x in be:
        if(x["type"] == "deployment"):
            x.pop("type")
            update_deployment(x, kind_name["deployment"], ns_path, tier)



def update_deployment(values, kind_name, ns_path, tier):
    print(values, kind_name, ns_path, tier)
    for k,v  in values.items():
        if(k == "replicas"):
            patch_deployment(ns_path, k, v, kind_name, tier)

def patch_deployment(ns_path, key, value, kind_name, tier):
    kustomize_path = ns_path + "kustomization.yaml"
    with open(kustomize_path) as file:
            kustomization = yaml.load(file, Loader=yaml.FullLoader)
    
    if "patches" not in kustomization.keys():
        entry = [{"target": {"name" : kind_name, "labelSelector" : "tier="+tier}, "path" : tier+"_"+kind_name+"_patch.yaml"}]
        kustomization["patches"] = entry
        with open(kustomize_path, "w") as file:
            yaml.dump(kustomization, file)
    else:
        found = False
        for entry in kustomization["patches"]:
            if entry["path"] == tier+"_"+kind_name+"_patch.yaml":
                found = True
            if found == False:
                entry = [{"target": {"name" : kind_name, "labelSelector" : "tier="+tier}, "path" : tier+"_"+kind_name+"_patch.yaml"}]
                kustomization["patches"] = entry
                with open(kustomize_path, "w") as file:
                    yaml.dump(kustomization, file)
    
    #adesso devo aggiungere il file patch.yaml
    found = False
    for filename in os.listdir(ns_path):
        if filename == tier+"_"+kind_name+"_patch.yaml":
            found = True
    if(found == False):
        with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "x") as file:
            patch = yaml.load(file, Loader=yaml.FullLoader)
    else:
        with open(ns_path+tier+"_"+kind_name+"_patch.yaml") as file:
            patch = yaml.load(file, Loader=yaml.FullLoader)

    if(key == "replicas"):
        if(patch != None):
            for ele in patch:
                found = False
                if(ele["path"] == "/spec/replicas"):
                    ele["value"] = value
                    found = True
            if(found == False):
                patch.append(dict({"op" : "add", "path" : "/spec/replicas", "value" : 33}))
            with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "w") as file:
                yaml.dump(patch, file)
        else:
            patch = [{"op" : "add", "path" : "/spec/replicas", "value" : 33}]
            with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "w") as file:
                yaml.dump(patch, file)
    

def update_service(values, kind_name, ns_path, tier):
    for k,v  in values.items():
        if(k == "port"):
            patch_service(ns_path, k, v, kind_name, tier)

def patch_service(ns_path, key, value, kind_name, tier):
    ns_path = "kustomize/overlay/prod/"
    kustomize_path = ns_path + "kustomization.yaml"
    with open(kustomize_path) as file:
            kustomization = yaml.load(file, Loader=yaml.FullLoader)
    
    if "patches" not in kustomization.keys():
        entry = [{"target": {"name" : kind_name, "labelSelector" : "tier="+tier}, "path" : tier+"_"+kind_name+"_patch.yaml"}]
        kustomization["patches"] = entry
        with open(kustomize_path, "w") as file:
            yaml.dump(kustomization, file)
    else:
        found = False
        for entry in kustomization["patches"]:
            if entry["path"] == tier+"_"+kind_name+"_patch.yaml":
                found = True
            if found == False:
                entry = [{"target": {"name" : kind_name, "labelSelector" : "tier="+tier}, "path" : tier+"_"+kind_name+"_patch.yaml"}]
                kustomization["patches"] = entry
                with open(kustomize_path, "w") as file:
                    yaml.dump(kustomization, file)
    
    #adesso devo aggiungere il file patch.yaml
    found = False
    for filename in os.listdir(ns_path):
        if filename == tier+"_"+kind_name+"_patch.yaml":
            found = True
    if(found == False):
        with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "x") as file:
            patch = yaml.load(file, Loader=yaml.FullLoader)
    else:
        
        with open(ns_path+tier+"_"+kind_name+"_patch.yaml") as file:
            patch = yaml.load(file, Loader=yaml.FullLoader)

    if(key == "replicas"):
        if(patch != None):
            for ele in patch:
                found = False
                if(ele["path"] == "/spec/replicas"):
                    ele["value"] = value
                    found = True
            if(found == False):
                patch.append(dict({"op" : "add", "path" : "/spec/replicas", "value" : 33}))
            with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "w") as file:
                yaml.dump(patch, file)
        else:
            patch = [{"op" : "add", "path" : "/spec/replicas", "value" : 33}]
            with open(ns_path+tier+"_"+kind_name+"_patch.yaml", "w") as file:
                yaml.dump(patch, file)