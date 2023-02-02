import json


def json_load_wrapper(arg_file):
    fid = open(arg_file, "r")
    d = json.load(fid)
    for k, v in d.items():
        if v == 'none':
            d[k] = None
    return d


if __name__ == '__main__':
    arg_file = "simple_safety_example.json"
    d = json_load_wrapper(arg_file)
    # for k, v in d.items():
    # print(str(k) + " : " + str(v))
    print(d)
