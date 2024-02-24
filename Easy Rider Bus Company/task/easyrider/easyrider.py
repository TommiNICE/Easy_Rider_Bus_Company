import json

data = input()
json_data = json.loads(data)

def on_demand(json_data):

    transfer = {i["stop_name"]: [] for i in json_data}
    for i in json_data:
        transfer[i["stop_name"]] += [i["bus_id"]]
    transfer = [i for i in transfer if len(transfer[i]) > 1]
    transfer_set = set(transfer)
    
    set_stop_type_O = set()
    for i in json_data:
        if i["stop_type"] == "O":
            set_stop_type_O.add(i["stop_name"])

    not_on_demand_set = sorted(set_stop_type_O.intersection(transfer_set))
    list_not_on_demand_set = list(not_on_demand_set)
    if not_on_demand_set:
        print("On demand stops test: ")
        print("Wrong stop type: " + str(list_not_on_demand_set))
    else:
        print("On demand stops test: ")
        print("Wrong stop type: OK")


on_demand(json_data)