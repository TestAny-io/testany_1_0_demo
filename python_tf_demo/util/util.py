import json
import re
import os
import configparser
import time
import requests

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    except RuntimeError as e:
        return False
    return True

def turn_str(text):
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    if is_json(text):
        text = json.loads(text)
    return text

def post_data(self, url, request_data=None, headers=None, proxies=None, result_exception=None, params=None, files=None):
        try:
                now = round(time.time(), 3)*1000
                r = requests.post(url, data=request_data, headers=headers, proxies=proxies, timeout=(300, 120), params=params, files=files)
                elapsed = round(time.time(), 3)*1000  #now + r.elapsed
        except Exception as e:
            raise e
        return r, str(now), str(elapsed)

def get_data(self, url, request_data=None, headers=None, proxies=None, result_exception=None, params=None, verify=None):
        try:
                now = round(time.time(), 3)*1000
                r = requests.get(url, data=request_data, headers=headers, proxies=proxies, timeout=(300, 120), params=params, verify=verify)
                elapsed = round(time.time(), 3)*1000  #now + r.elapsed
        except Exception as e:
            raise e
        return r, str(now), str(elapsed)

def delete_jsonfile(filename):
    config = configparser.ConfigParser()
    current_path = os.path.abspath(__file__)
    file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), 'config.ini')
    config.read(file_path)
    confi_valu = config.get('testjson', 'testdir')
    filepath = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), confi_valu, filename)
    if os.path.exists(filepath):
        os.remove(filepath)


def save_jsonfile_to_dir(filename, string):
    config = configparser.ConfigParser()
    current_path = os.path.abspath(__file__)
    file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), 'config.ini')
    config.read(file_path)
    confi_valu = config.get('testjson', 'testdir')
    filepath = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), confi_valu, filename)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as json_file:
            test_result = {"testOutputs": []}
            json_file.write(str(json.dumps(test_result, ensure_ascii=False)))
    with open(filepath, "r", encoding="utf-8") as str_file:
        test_result = str_file.read()
        # print(string)
        if len(test_result) <= 19:
            test_output = test_result[:-2]+string + "]}"
        if len(test_result) > 19:
            test_output = test_result[:-2] + ", "+string + "]}"
        # print(test_output)
    with open(filepath, "w", encoding="utf-8") as json_file:
        json_file.write(str(test_output))


def json_string(stepname, input, output, result, assertion):
    if len(output) == 2:
        http_method = output[1].request.method
        if is_json(output[1].text):
            output_content = json.loads(output[1].text)
        elif output[1].text is None:
            output_content = ""
        else:
            output_content = str(output[1].text)
    else:
        output_content = str(output[2])
        http_method = None

    str2 = {
        "name": stepname,
        "httpMethod": http_method,
        "input": {
            "triggerTime": float(input[0]),   
            "requestUrl": input[1],
            "requestHeader":  str(input[2]), 
            "requestBody": str(input[3]), 
        },
        "output": {
            "receiveTime": float(output[0]),   
            "responseBody": str(output_content), 
        },
        "result": result
    }
    assertions = []
    i = 0
    for lists in assertion:
        print(lists[1])
        if type(lists[1]) in [str, int, list, dict, float]:
            if str(lists[1]) in str(lists[2]):
                assertResult = "Passed"
            elif str(lists[2]) in str(lists[1]):
                assertResult = "Passed"
            else:
                assertResult = "Failed"
        elif type(lists[1]) is bool:
            if lists[1] is True and lists[2] is not None:
                assertResult = "Passed"
            elif lists[1] is False and lists[2] is None:
                assertResult = "Passed"
            else:
                assertResult = "Failed"
        else:
            assertResult = "Failed"
        field = {"field": str(lists[0]),
                "expectedValue": str(lists[1]),
                "actualValue": str(lists[2]),
                "assertionsResult": assertResult}
        assertions.append(field)
        i = i+1
    str2["assertions"] = assertions
    json_str = json.dumps(str2)
    json_str = re.sub(": None", ": null", json_str)
    json_str = re.sub(": True", ": true", json_str)
    json_str = re.sub(": False", ": false", json_str)
    print(json.dumps(json_str, ensure_ascii=False))
    return json_str
