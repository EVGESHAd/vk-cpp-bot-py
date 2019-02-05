import json
from random import randint as rand
outMsg['message']='земля ему пухом'
if user_get(user_id)==1:
    if rand(0,100)<40:
        outMsg["attachment"]=vk_upload("py/357_shot1.wav", outMsg["peer_id"], "audio_message")
        vk_send('messages.send', outMsg, 1)
        outMsg={}
        vk_send('messages.removeChatUser', {'chat_id':str(chat_id), 'user_id':str(user_id)}, 1)
    else:
        outMsg["attachment"]=vk_upload("py/357_shot1.wav", outMsg["peer_id"], "audio_message")
        vk_send('messages.send', outMsg, 1)
        outMsg["attachment"]=vk_upload("py/357_reload1.wav", outMsg["peer_id"], "audio_message")
        outMsg['message']='живучий попался'
        vk_send('messages.send', outMsg, 1)
        outMsg={}
else:
	try:
		id=''
		try:
			id=str(json.loads(vk_send('messages.getById', {'message_ids':str(msg_id)}, 1))['response']['items'][0]['fwd_messages'][0]['user_id'])
		except:
			id=msg.split('/')[-1].split('|')[0].replace('[', '').replace('@', '')
			id=str(json.loads(vk_send('users.get',{'user_ids':id},1))['response'][0]['id'])
		outMsg["attachment"]=vk_upload("py/357_shot1.wav", outMsg["peer_id"], "audio_message");
		vk_send('messages.send', outMsg, 1)
		json.loads(vk_send('messages.removeChatUser', {'chat_id':str(chat_id), 'user_id':id}, 1))['response']
		outMsg={'peer_id':outMsg['peer_id']}
	except:
		outMsg['message']='¯\\_(ツ)_/¯'
		outMsg["attachment"]=vk_upload("py/357_reload1.wav", outMsg["peer_id"], "audio_message")
