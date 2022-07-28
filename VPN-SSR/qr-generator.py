import base64
import qrcode

##SSR Configuration
server='ip'
server_port=(12384).__str__()
password=base64.urlsafe_b64encode(('password').encode(encoding="utf-8")).decode().replace('=','')
protocol='auth_chain_a'
protoparam=''
method='aes-256-cfb'
obfs='tls1.2_ticket_auth'
obfsparam=''
remarks=''
group=''

##SSR Parameters
main_part = server + ":" + server_port + ":" + protocol + ":" + method + ":" + obfs + ":" + password

## Old Parameter
#param_str = 'obfsparam=' + base64.urlsafe_b64encode(obfsparam.encode(encoding="utf-8")).decode().replace('=','')\
#+'&remarks=' + base64.urlsafe_b64encode(remarks.encode(encoding="utf-8")).decode().replace('=','')\
#+'&group=' + base64.urlsafe_b64encode(group.encode(encoding="utf-8")).decode().replace('=','')


# To decode:
# base64.b64decode(a.encode())

param_str = 'obfsparam=' + base64.urlsafe_b64encode(obfsparam.encode(encoding="utf-8")).decode().replace('=','')\
+'&protoparam=' + base64.urlsafe_b64encode(protoparam.encode(encoding="utf-8")).decode().replace('=','')\
+'&remarks=VnBOeWFu' \
+'&group=' + base64.urlsafe_b64encode(group.encode(encoding="utf-8")).decode().replace('=','')




shareqrcode_str = "ssr://"+base64.urlsafe_b64encode((main_part + "/?" + param_str).encode(encoding="utf-8")).decode().replace('=','');

print(main_part + "/?" + param_str)
print(shareqrcode_str)

##QR Generator
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=8,
    border=4,
)
filename = 'qrcode.png'
qr.add_data(shareqrcode_str)
qr.make(fit=True)
img = qr.make_image()
img.save(filename)
