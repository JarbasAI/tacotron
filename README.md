# Tacotron

An implementation of Tacotron speech synthesis in Tensorflow.
Modification to python2 implementation of author keithito, [github](https://github.com/keithito/tacotron).

### Audio Samples

  * **[Audio Samples](https://keithito.github.io/audio-samples/)** after training for 877k steps (~11 days).
    * Speech started to become intelligble around 20k steps.
    * There hasn't been much improvement since around 200k steps -- loss has gone down, but it's hard to notice
      listening to the audio.


## Background

Earlier this year, Google published a paper, [Tacotron: A Fully End-to-End Text-To-Speech Synthesis Model](https://arxiv.org/pdf/1703.10135.pdf),
where they present a neural text-to-speech model that learns to synthesize speech directly from
(text, audio) pairs. However, they didn't release their source code or training data. This is an
attempt to provide an open-source implementation of the model described in their paper.

The quality isn't as good as Google's demo yet, but hopefully it will get there someday :-).
Pull requests are welcome!



## Quick Start

### Installing dependencies
Make sure you have Python 3. Then:
```
pip install -r requirements.txt
```


### Using a pre-trained model

1. **Download and unpack a model**:
   ```
   curl http://data.keithito.com/data/speech/tacotron-20170720.tar.bz2 | tar x -C /tmp
   ```

2. **Run the demo server**:
   ```
   python demo_server.py --checkpoint /tmp/tacotron-20170720/model.ckpt
   ```

3. **Point your browser at localhost:9000**
   * Type what you want to synthesize



### Training

*Note: you need at least 40GB of free disk space to train a model.*

1. **Download a speech dataset.**

   The following are supported out of the box:
    * [LJ Speech](https://keithito.com/LJ-Speech-Dataset/) (Public Domain)
    * [Blizzard 2012](http://www.cstr.ed.ac.uk/projects/blizzard/2012/phase_one) (Creative Commons Attribution Share-Alike)

   You can use other datasets if you convert them to the right format. See [TRAINING_DATA.md](TRAINING_DATA.md) for more info.


2. **Unpack the dataset into `~/tacotron`**

   After unpacking, your tree should look like this for LJ Speech:
   ```
   tacotron
     |- LJSpeech-1.0
         |- metadata.csv
         |- wavs
   ```

   or like this for Blizzard 2012:
   ```
   tacotron
     |- Blizzard2012
         |- ATrampAbroad
         |   |- sentence_index.txt
         |   |- lab
         |   |- wav
         |- TheManThatCorruptedHadleyburg
             |- sentence_index.txt
             |- lab
             |- wav
   ```

3. **Preprocess the data**
   ```
   python preprocess.py --dataset ljspeech
   ```
     * Use `--dataset blizzard` for Blizzard data

4. **Train a model**
   ```
   python train.py
   ```

5. **Monitor with Tensorboard** (optional)
   ```
   tensorboard --logdir ~/tacotron/logs-tacotron
   ```

   The trainer dumps audio and alignments every 1000 steps. You can find these in
   `~/tacotron/logs-tacotron`.

6. **Synthesize from a checkpoint**
   ```
   python demo_server.py --checkpoint ~/tacotron/logs-tacotron/model.ckpt-185000
   ```
   Replace "185000" with the checkpoint number that you want to use, then open a browser
   to `localhost:9000` and type what you want to speak. Alternately, you can
   run [eval.py](eval.py) at the command line:
   ```
   python eval.py --checkpoint ~/tacotron/logs-tacotron/model.ckpt-185000
   ```


## Miscellaneous Notes

  * [TCMalloc](http://goog-perftools.sourceforge.net/doc/tcmalloc.html) seems to improve
    training speed and avoids occasional slowdowns seen with the default allocator. You
    can enable it by installing it and setting `LD_PRELOAD=/usr/lib/libtcmalloc.so`.

  * You can train with [CMUDict](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) by downloading the
    dictionary to ~/tacotron/training and then passing the flag `--hparams="use_cmudict=True"` to
    train.py. This will allow you to pass ARPAbet phonemes enclosed in curly braces at eval
    time to force a particular pronunciation, e.g. `Turn left on {HH AW1 S S T AH0 N} Street.`

  * If you pass a Slack incoming webhook URL as the `--slack_url` flag to train.py, it will send
    you progress updates every 1000 steps.

  * Occasionally, you may see a spike in loss and the model will forget how to attend (the
    alignments will no longer make sense). Although it will recover eventually, it may
    save time to restart at a checkpoint prior to the spike by passing the
    `--restore_step=150000` flag to train.py (replacing 150000 with a step number prior to the
    spike). **Update**: a recent [fix](https://github.com/keithito/tacotron/pull/7) to gradient
    clipping by @candlewill may have fixed this.


## Other Implementations
  * By Alex Barron: https://github.com/barronalex/Tacotron
  * By Kyubyong Park: https://github.com/Kyubyong/tacotron
