from flask import Flask, render_template, redirect, request

import Caption_it

from gtts import gTTS
import os
import IPython

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		f.save(path)

		caption = Caption_it.caption_this_image(path)

		#voice generation

		language = 'en'
  
		myobj = gTTS(text=caption, lang=language, slow=False)
		path_voice = "./static/{}.mp3".format(f.filename)
		myobj.save(path_voice)
  
		#os.system("start output.mp3")
		#IPython.display.Audio('output.mp3')
		
		result_dic = {
		'image' : path,
		'caption' : caption,
		'voice' : path_voice
		}

	return render_template("index.html", your_result=result_dic)

if __name__ == '__main__':
	# app.debug = True
	app.run(debug = True)