from synthesizer import Synthesizer
from os.path import dirname
import time

model = "tacotron-20170720"
path = dirname(__file__) + "/trained/" + model + "/model.ckpt"

synthesizer = Synthesizer()
synthesizer.load(path)

texts = ["bitcoin is the future",
         "long live the blockchain",
         "i love artificial intelligence",
         "my name is Jarbas and i am an open source artificial intelligenc"]

for text in texts:
    start = time.time()
    out = dirname(__file__) + "/output_samples/" + text.replace(" ",
                                                                "_") + ".wav"
    synthesizer.synthesize(text, out)

    print "input", text
    print "output_path", out
    print "elapsed time", time.time() - start
