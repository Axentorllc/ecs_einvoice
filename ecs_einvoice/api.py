from __future__ import unicode_literals
from re import A
import frappe
from frappe import auth
import datetime
import json, ast, requests
from frappe.utils import money_in_words
import urllib.request


#url = 'https://system.classatrading.com/api/method/classa.functions.sales_invoice_add'
#headers = {'content-type': 'application/json; charset=utf-8'}
#response = requests.post(url, json=data , headers=headers)
#frappe.msgprint(response.text)

frappe.whitelist()
def login():
    api_base_url = frappe.db.get_single_value('EInvoice Settings', 'api_base_url')
    id_server_base_url = frappe.db.get_single_value('EInvoice Settings', 'id_server_base_url')
    client_id = frappe.db.get_single_value('EInvoice Settings', 'client_id')
    client_secret = frappe.db.get_single_value('EInvoice Settings', 'client_secret')
    generated_access_token = frappe.db.get_single_value('EInvoice Settings', 'generated_access_token')

    
    #url = 'https://system.classatrading.com/api/method/classa.functions.sales_invoice_add'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(id_server_base_url, data={
        'grant_type':'client_credentials',
        'client_id':client_id,
        'client_secret':client_secret,
        'scope': 'InvoicingAPI'
    } , headers=headers)
    #message = response.text(access_token)
    #print(response.json[key])
    json = response.json()
    token = ""
    for key in json:
        if key == "access_token":
            #token = json[key]
            frappe.db.sql(""" update `tabSingles` set value = '{new_token}' where doctype= 'EInvoice Settings' and field = 'generated_access_token' """.format(new_token=json[key]))
    #print(response.status_code)
    #print(response.content)
    #frappe.msgprint(api_base_url)
    pass

frappe.whitelist()
def submit_invoice():
    api_base_url = frappe.db.get_single_value('EInvoice Settings', 'api_base_url')
    id_server_base_url = frappe.db.get_single_value('EInvoice Settings', 'id_server_base_url')
    client_id = frappe.db.get_single_value('EInvoice Settings', 'client_id')
    client_secret = frappe.db.get_single_value('EInvoice Settings', 'client_secret')
    generated_access_token = frappe.db.get_single_value('EInvoice Settings', 'generated_access_token')




    data={}
    data["documentType"] = "I"
    data["documentTypeVersion"]="0.9"
    data["taxpayerActivityCode"] = frappe.db.get_single_value('EInvoice Settings', 'activity_code') 
    data["signatures"] =  {
               "signatureType":"I",
               "value":"MIIGywYJKoZIhvcNAQcCoIIGvDCCBrgCAQMxDTALBglghkgBZQMEAgEwCwYJKoZIhvcNAQcFoIID/zCCA/swggLjoAMCAQICEEFkOqRVlVar0F0n3FZOLiIwDQYJKoZIhvcNAQELBQAwSTELMAkGA1UEBhMCRUcxFDASBgNVBAoTC0VneXB0IFRydXN0MSQwIgYDVQQDExtFZ3lwdCBUcnVzdCBDb3Jwb3JhdGUgQ0EgRzIwHhcNMjAwMzMxMDAwMDAwWhcNMjEwMzMwMjM1OTU5WjBgMRUwEwYDVQQKFAxFZ3lwdCBUcnVzdCAxGDAWBgNVBGEUD1ZBVEVHLTExMzMxNzcxMzELMAkGA1UEBhMCRUcxIDAeBgNVBAMMF1Rlc3QgU2VhbGluZyBEZW1vIHVzZXIyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApmVGVJtpImeq\u002BtIJiVWSkIEEOTIcnG1XNYQOYtf5\u002BDg9eF5H5x1wkgR2G7dvWVXrTsdNv2Q\u002Bgvml9SdfWxlYxaljg2AuBrsHFjYVEAQFI37EW2K7tbMT7bfxwT1M5tbjxnkTTK12cgwxPr2LBNhHpfXp8SNyWCxpk6eyJb87DveVwCLbAGGXO9mhDj62glVTrCFit7mHC6bZ6MOMAp013B8No9c8xnrKQiOb4Tm2GxBYHFwEcfYUGZNltGZNdVUtu6ty\u002BNTrSRRC/dILeGHgz6/2pgQPk5OFYRTRHRNVNo\u002BjG\u002BnurUYkSWxA4I9CmsVt2FdeBeuvRFs/U1I\u002BieKg1wIDAQABo4HHMIHEMAkGA1UdEwQCMAAwVAYDVR0fBE0wSzBJoEegRYZDaHR0cDovL21wa2ljcmwuZWd5cHR0cnVzdC5jb20vRWd5cHRUcnVzdENvcnBvcmF0ZUNBRzIvTGF0ZXN0Q1JMLmNybDAdBgNVHQ4EFgQUqzFDImtytsUbghbmtnl2/k4d5jEwEQYJYIZIAYb4QgEBBAQDAgeAMB8GA1UdIwQYMBaAFCInP8ziUIPmu86XJUWXspKN3LsFMA4GA1UdDwEB/wQEAwIGwDANBgkqhkiG9w0BAQsFAAOCAQEAxE3KpyYlPy/e3\u002B6jfz5RqlLhRLppWpRlKYUvH1uIhCNRuWaYYRchw1xe3jn7bLKbNrUmey\u002BMRwp1hZptkxFMYKTIEnNjOKCrLmVIuPFcfLXAQFq5vgLDSbnUhG/r5D\u002B50ndPucyUPhX3gw8gFlA1R\u002BtdNEoeKqYSo9v3p5qNANq12OuZbkhPg6sAD4dojWoNdlkc8J2ML0eq4a5AQvb4yZVb\u002BezqJyqKj83RekRZi0kMxoIm8l82CN8I/Bmp6VVNJRhQKhSeb7ShpdkZcMwcfKdDw6LW02/XcmzVl8NBBbLjKSJ/jxdL1RxPPza7RbGqSx9pfyav5\u002BAxO9sXnXXc5jGCApIwggKOAgEBMF0wSTELMAkGA1UEBhMCRUcxFDASBgNVBAoTC0VneXB0IFRydXN0MSQwIgYDVQQDExtFZ3lwdCBUcnVzdCBDb3Jwb3JhdGUgQ0EgRzICEEFkOqRVlVar0F0n3FZOLiIwCwYJYIZIAWUDBAIBoIIBCjAYBgkqhkiG9w0BCQMxCwYJKoZIhvcNAQcFMBwGCSqGSIb3DQEJBTEPFw0yMTAyMDEyMzUwMjFaMC8GCSqGSIb3DQEJBDEiBCD5bGXJu9uJZIPMGXK98UrHzJM/V2U/WAO6BErxpX5wdTCBngYLKoZIhvcNAQkQAi8xgY4wgYswgYgwgYUEIAJA8uO/ek3l9i3ZOgRtPhGWwwFYljbeJ7yAgEnyYNCWMGEwTaBLMEkxCzAJBgNVBAYTAkVHMRQwEgYDVQQKEwtFZ3lwdCBUcnVzdDEkMCIGA1UEAxMbRWd5cHQgVHJ1c3QgQ29ycG9yYXRlIENBIEcyAhBBZDqkVZVWq9BdJ9xWTi4iMAsGCSqGSIb3DQEBAQSCAQB13E1WX\u002BzbWppfJi3DBK9MMSB1TXuxcNkGXQ19OcRUUAaAe2K\u002BisobYrUCZbi3ygc2AWOMyafboxjjomzrnvXKrFgspT4wAFPYaAGFzKWq\u002BW/nqMhIqJVIpS/NM7Al4HvuBA5iGuZEQFusElB0yIxOIiYDI4v8Ilkff4/duj/V2CNaN5cqXLOpL5RP6Y5i\u002BVsPGb89t/L0dSIldGN0JqaqarqYo5/RwsUFJJq01DFpPGNbOIX3gSCDmycfhJPS9csnne9Zt\u002BabNpja5ZR6KA8JMe4DHes7FDZqHBNHdC\u002BRDXT4crqmnyiJjizULu6MqDc0Fv3vrMMWDLRlwDecgq7i"
            }

    headers = {'content-type': 'application/json;charset=utf-8',
    "Authorization":"Bearer" + generated_access_token,
    "Content-Length" : "376"
    }
    response = requests.post(api_base_url, json=data  , headers=headers)
    print(response.text)
    print(response.status_code)
    print(response.content)
    #print(generated_access_token)
    #frappe.msgprint(api_base_url)
    pass
