import random
import untangle
import os
r34text = '-fur+-scat*+-darling_in_the_franxx+-furry+-dragon+-guro+-animal_penis+-animal+-wolf+-fox+-webm+-my_little_pony+-monster*+-3d+-animal*+-ant+-insects+-mammal+-horse+-blotch+-deer+-real*+-shit+-everlasting_summer+-copro*+-wtf+-censored+' + msg.replace(' ','+')
r34text=msg.replace(' ','+')
r34text = '-fur+-scat*+-furry+-dragon+-guro+-animal_penis+-animal+-wolf+-fox+-webm+-my_little_pony+-monster*+-animal*+-ant+-insects+-mammal+-horse+-blotch+-deer+-real*+-shit+-everlasting_summer+-copro*+-wtf+-censored+' + msg.replace(' ','+')
outMsg['message']=''
outMsg['attachment']=''
try:
	resp = untangle.parse(net_send('http://0s.oj2wyzjtgqxhq6dy.cmle.ru/index.php?page=dapi&s=post&limit=10000&q=index&tags='+str(r34text), {}, 1)).posts.post
	if not os.path.exists('34'):
		os.mkdir('34')
	indexs=list(range(len(resp)))
	random.shuffle(indexs)
	for i in indexs[0:4]:
		#outMsg['message']+=str(i+1)+'/'+str(len(resp))+'\n'+str(resp[i]['tags'])+'\n\n'
		net_download(str(resp[i]['file_url']), '34/'+str(msg_id)+'_'+str(i)+'.jpg', '')
		outMsg['attachment']+=vk_upload('34/'+str(msg_id)+'_'+str(i)+'.jpg', outMsg['peer_id'], 'photo')+','
except Exception as e:
	outMsg['message']+=e