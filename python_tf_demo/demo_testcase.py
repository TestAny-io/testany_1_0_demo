import unittest
import json
from util.util import post_data, get_data, turn_str, json_string, delete_jsonfile, save_jsonfile_to_dir

proxies=None

class TestDemo(unittest.TestCase):
    def test_post1(self, json_file_name):
        headers = {
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        body = {"property" : ["Sites"], "report_type" : ["ALL"]}
        url = "http://ip.jsontest.com/"
        request_data = json.dumps(body)
        result_exception="Sorry, you can not get the IP Address !"
        r, now, elapsed = post_data(self, url, request_data, headers, proxies , result_exception)
        r_json = json.loads(r.text)
        if r.status_code == 200:
            result = "Pass"
            response_error = None
        else:
            result = "Fail"
            url_error = "ERROR_URL: " + url
            response_error = "ERROR_RESPONSE: " + r.text

        if "Pass" in result:
            case_result = "Success"
        else:
            case_result = "Failure"
        text = turn_str(r.text)
        str2 = json_string("step-1-POST-Get_IP_Address", [now, url, headers, body], [elapsed, r], case_result, [["HTTP status_code", 200, r.status_code]])
        save_jsonfile_to_dir(json_file_name, str(str2))
        self.assertEqual(200, r.status_code)

    def test_get1(self, json_file_name):
        headers = {
            "Content-Type": "application/json",
            "Connection": "keep-alive"#,
            #"Host": "ip.jsontest.com"
        }
        body = None
        url = "http://ip.jsontest.com/"
        request_data = None
        result_exception="Sorry, you can not get the IP Address !"
        r, now, elapsed = get_data(self, url, request_data, headers, proxies , result_exception)
        print(r.text)
        r_json = json.loads(r.text)
        if r.status_code == 200:
            result = "Pass"
            response_error = None
        else:
            result = "Fail"
            url_error = "ERROR_URL: " + url
            response_error = "ERROR_RESPONSE: " + r.text

        if "Pass" in result:
            case_result = "Success"
        else:
            case_result = "Failure"
        text = turn_str(r.text)
        str2 = json_string("step-2-GET-Get_IP_Address", [now, url, headers, body], [elapsed, r], case_result, [["HTTP status_code", 200, r.status_code]])
        save_jsonfile_to_dir(json_file_name, str(str2))
        self.assertEqual(200, r.status_code)

    def test_post3(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_demo1(self):
        json_file_name= "test_demo1.json"
        delete_jsonfile(json_file_name)
        self.test_post1(json_file_name)
        self.test_get1(json_file_name)
        #test_post3(json_file_name)

if __name__ == '__main__':
    unittest.main()
