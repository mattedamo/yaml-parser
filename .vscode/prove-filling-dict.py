
import yaml

final = {}
final["patches"] = [{"target" : {"desenzano" : "smaug", "smigol" : 1} , "path": "salamon"}]
print(final)

with open("patch.yaml") as file:
            patch = yaml.load(file, Loader=yaml.FullLoader)
print(patch)