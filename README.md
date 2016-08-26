ReSpeaker Adapter
=============

Use your voice to control a power adapter. Make Home Automation easier.

mic > keyword spotting (pocketsphinx) > stt (bing) > text parser > Wio Node > Grove - Relay	
								 > tts > speaker

### Get started
1. Get [pocketsphinx acoustic model](https://github.com/respeaker/pocketsphinx_keyword_spotting/tree/master/model/hmm), place the files as the following structure.

  ```
  respeaker_hi
  │  bing_recognizer.py
  │  creds_template.py
  │  main.py
  │  microphone.py
  │  player.py
  |  relay.py
  │  README.md
  ├─audio
  │      hi.wav
  └─model
      │  respeaker.dic
      └─hmm
          └─en
                  feat.params
                  mdef
                  means
                  noisedict
                  README
                  sendump
                  transition_matrices
                  variances
  ```
  
2. Get a key from # get a key from https://www.microsoft.com/cognitive-services/en-us/speech-api and create creds.py with the key

3. Add your own Wio access_token to 'main.py'

4. `python main.py`
