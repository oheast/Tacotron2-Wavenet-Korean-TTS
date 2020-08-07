# coding: utf-8
import os
import codecs
import shutil
import json

kss_path = '../../../data/speech/korean-single-speaker-speech-dataset'

with open(os.path.join(kss_path, 'transcript.v.1.4.txt'), 'r', encoding='utf-8') as t:
	raw_text = t.readlines()

audio_list = []
text_list = []
for r in raw_text:
	split_raw = r.split('|')
	audio_list.append(split_raw[0])
	text_list.append(split_raw[2])

print(audio_list[0:3])
print(text_list[0:3])

tacotron_path = 'datasets/kss'

if not os.path.exists(tacotron_path):
	os.mkdir(tacotron_path)
	os.mkdir(os.path.join(tacotron_path, 'audio'))

with open(os.path.join(tacotron_path, 'kss-recognition-All.json'), 'w') as f:
	f.write('{\n')	
	for audio, text in zip(audio_list, text_list):
		shutil.copy(os.path.join(kss_path,'kss', audio),
				os.path.join(tacotron_path, 'audio', audio[2:]))
		f.write('\t'+'"'+'./'+os.path.join(tacotron_path,'audio',audio[2:])+'"'\
				+': '+'"'+text+'"'+',\n')
	f.write('}')

print('Finsh')
