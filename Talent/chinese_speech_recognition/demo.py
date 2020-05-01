#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform as plat

from SpeechModel251 import ModelSpeech
from LanguageModel2 import ModelLanguage
from keras import backend as K
from glob import glob
speech_files = glob('./demovedio/*.*')

datapath = ''
modelpath = 'model_speech'

system_type = plat.system() # 由于不同的系统的文件路径表示不一样，需要进行判断
if(system_type == 'Windows'):
	datapath = 'dataset'
	modelpath = modelpath + '\\'
elif(system_type == 'Linux'):
	datapath = 'dataset'
	modelpath = modelpath + '/'
else:
	print('*[Message] Unknown System\n')
	datapath = 'dataset'
	modelpath = modelpath + '/'

ms = ModelSpeech(datapath)

#ms.LoadModel(modelpath + 'm22_2\\0\\speech_model22_e_0_step_257000.model')
ms.LoadModel(modelpath + 'speech_model251_e_0_step_625000.model')
ml = ModelLanguage('model_language')
#ms.TestModel(datapath, str_dataset='test', data_count = 64, out_report = True)
#r = ms.RecognizeSpeech_FromFile('E:\\github\\ASRT_SpeechRecognition\\dataset\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav')
#r = ms.RecognizeSpeech_FromFile('D:\语音数据集\ST-CMDS-20170001_1-OS\\20170001P00241I0053.wav')
#r = ms.RecognizeSpeech_FromFile('D:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00020I0087.wav')
#r = ms.RecognizeSpeech_FromFile('D:\\语音数据集\\data_thchs30\\data\\A11_167.WAV')
#r = ms.RecognizeSpeech_FromFile('D:\\语音数据集\\data_thchs30\\data\\D4_750.wav')
for speech_file in sorted(speech_files):
	print(speech_file)
	
	ml.LoadModel()
	r = ms.RecognizeSpeech_FromFile(speech_file)
	K.clear_session()
	print('*[提示] 语音识别结果：\n',r)
	str_pinyin = r

	r = ml.SpeechToText(str_pinyin)
	print('语音转文字结果：\n',r)
	# break













