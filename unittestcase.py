import requests
import unittest


class AppUnitTest(unittest.TestCase):
    
    #Table deletion testcase
    def test_vanishtable(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/deletetable"
            payload={}
            files=[]
            headers = {}
            response = requests.request("DELETE", url, headers=headers, data=payload, files=files)
        except Execution as e:
            print('Exception occured while delete the table {}'.format(e))
        finally:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.text,"table deleted succesfully")
            
    #Test case for insert an url
    def test_insertrecord(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/add"
            inserturl = "www.yahoo.com"
            payload={'insert_url': inserturl}
            files=[]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)                  
        except Exception as e:
            print('Exception occurred while testing inserting the record{}'.format(e))
        finally:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.text,"the insert_url is "+inserturl)
            
    # Test case for update a record 
    def test_updaterecord(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/1"
            updateurl = "www.google.com"
            id=url.rsplit('/',1)[-1]
            payload={'update_url': updateurl}
            files=[]
            headers = {}
            response = requests.request("PUT", url, headers=headers, data=payload, files=files)
        except Exception as e:
            print('Exception occured while testing updating the record{}'.format(e))
        finally:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.text,"url id with "+id+" is updated with url string "+updateurl)

    # Test case for clearing the table values
    def test_vanishrecord(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/1"
            id=url.rsplit('/',1)[-1]
            payload={}
            files={}
            headers = {}
            response = requests.request("DELETE", url, headers=headers, data=payload, files=files)                    
        except Exception as e:
            print('Exception occurred while testing deleting the record{}'.format(e))
        finally:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.text,"url id with "+id+" is Deleted")
            
    # test case for checking whether an URL is present
    def test_urlcheck(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/isSafeUrl?hostname=www.google.com&port&originalpathquerystring"
            payload={}
            files=[]
            headers = {'Content-Type': 'application/json'}
            response = requests.request("GET", url, headers=headers, data=payload, files=files)            
        except Exception as e:
            print('Exception occurred while checking url {}'.format(e))
        finally:
            self.assertEqual(response.status_code,400)
            self.assertEqual(response.text,"The URL is unsafe")


if __name__ == '__main__' :
    domain = "http://192.168.0.105"
    port = "3200"
    unittest.main()
    
    
