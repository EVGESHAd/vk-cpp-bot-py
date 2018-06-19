s=msg.decode('utf-8')
out=''
for ch in s:
 out+=unichr(ord(ch)-1)
outMsg['message']=out.encode('utf-8')