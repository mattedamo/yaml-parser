# yaml-parser

## v0.0.1
The developer, can write a file yaml where he inserts values to apply in the infrastructure code, thanks to the py scripts. This script, in its first version,
is thought for a full stack application, then you must specify a namespace and values for the backend, frontend and database tiers.

### ns key
It must be specified and the possible values could be: ***prod, test, dev***. It depends on which branch are you working on.

```
ns : "prod" 
```

### backend/frontend keys
It is facoltative and can contain different type of sub-elements as list: ***deployment, service, secret***.

```
backend:
  - type: deployment
    replicas: 3
  - type: secret
    DB_PASSWORD: password
```

### db key
It is facoltative and can contain only ***secret*** as sub-element type.

### deployment type
Here the developer can specify the number of replicas

### service type
Here the developer can specify the sourcePort and the targetPort

### secret type
Here the developer can specify the list of secret as pairs **KEY : VALUE**

The script parse the input yaml file and update automatically the files into the kustomize folder. For what concerns about deployment and service, it generate
or update file into overlay/namespace folder
