import json
outMsg['message']=''
res=json.loads(net_send('https://ru.wikipedia.org/w/api.php',{'action':'opensearch','search':msg,'limit':'3','namespace':'0','format':'json'}, 1))
for i in range(len(res[2])):
 outMsg['message']+=res[1][i]+'\n'+res[2][i]+'\n( '+res[3][i]+' )\n\n'