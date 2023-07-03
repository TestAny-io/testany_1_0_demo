# testany_1_0_demo
## Test Case - Get your IP Address
### step1-POST-Get IP Address
Use `POST` request to get your current IP Address via `http://ip.jsontest.com/`
```
curl -X POST http://ip.jsontest.com -d '{"property" : ["Sites"], "report_type" : ["ALL"]}'
``` 
### step2-GET-Get IP Address
Use `GET` request to get your current IP Address via `http://ip.jsontest.com/`
```
curl -X GET http://ip.jsontest.com'
```

## Sample code
```
git clone https://github.com/TestAny-io/testany_1_0_demo.git
```

## TestCase with python test framework
### python test framework demo
```
cd python_tf_demo
```
### run the test case
```
python demo_testcase.py -k test_demo1 
```

## TestCase with java test framework
### java test framework demo
```
cd java_tf_demo
```
### test ca se json file
```
cd cases
cat demo_testcase.json
```
