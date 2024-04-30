import base64
kid=input("input KID:")
kid+=((4-(len(kid)%4))%4)*"="
key_value=input("input key_value:")
key_value+=((4-(len(key_value)%4))%4)*"="
kid=kid.replace("-","+").replace("_","/")
key_value=key_value.replace("-","+").replace("_","/")
res=base64.b64decode(kid)
keydecode=''.join(['%02x' % b for b in res])
res=base64.b64decode(key_value)
# print(res)
valuedecode=''.join(['%02x' % b for b in res])
print("{0}:{1}".format(keydecode,valuedecode))