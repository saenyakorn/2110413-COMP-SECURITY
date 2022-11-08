import json


def store_result(result: dict, name: str) -> None:
    with open(f'{name}.json', 'w') as f:
        json_string = json.dumps(result)
        f.write(json_string)


def load_result(name: str) -> None:
    with open(f'{name}.json', 'r') as f:
        json_string = f.read()
        result = json.loads(json_string)
        return result


def remove_result(name: str) -> None:
    import os
    os.remove(f'{name}.json')


if __name__ == '__main__':
    d = dict()
    d["aa"] = (121, 2)
    d["ab"] = (122, 2)
    d["ba"] = (123, 2)
    d["bb"] = (124, 2)

    print("Storing result")
    store_result(d, "test")

    print("Loading result")
    print(load_result("test"))

    print("Removing result")
    remove_result("test")
