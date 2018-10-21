net_download('https://github.com/FWGS/xash3d-deploy/blob/travis-master/xash3d-generic.apk?raw=true', 'xash3d.apkk', '')
outMsg['attachment']=vk_upload('xash3d.apkk', outMsg['peer_id'], 'doc')
outMsg['message']=net_send('https://raw.githubusercontent.com/FWGS/xash3d-deploy/travis-latest/README.md', {}, 0).split('```')[1]