aclNum = int(input("Cuál es el número IPv4 de ACL? "))
if aclNum >= 1 and aclNum <=99:
    print("Esta es una ACL IPv4 Estándar. ")
elif aclNum >= 100 and aclNum <= 199:
    print("Esta es una ACL IPv4 Extendida. ")
else:
    print("Esta ACL IPv4 no es Estándar o Extendida. ")