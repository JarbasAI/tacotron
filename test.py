from synthesizer import Synthesizer
from os.path import dirname, exists
from os import mkdir
import time

model = "tacotron-20170720"
path = dirname(__file__) + "/trained/" + model + "/model.ckpt"

synthesizer = Synthesizer()
synthesizer.load(path)

texts = ["bitcoin is the future",
         "long live the blockchain",
         "i love artificial intelligence",
         "my name is Jarbas and i am an open source artificial intelligence"]

base_out = dirname(__file__) + "/output_samples/"
if not exists(base_out):
    mkdir(base_out)

for text in texts:
    start = time.time()
    out = base_out + text.replace(" ", "_") + ".wav"
    synthesizer.synthesize(text, out)
    print "input", text
    print "output_path", out
    print "elapsed time", time.time() - start
