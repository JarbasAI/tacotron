from synthesizer import Synthesizer
from os.path import dirname
import time
model = "tacotron-20170720"
path = dirname(__file__) + "/trained/" + model + "/model.ckpt"
text = "support me on patreon"
synthesizer = Synthesizer()
synthesizer.load(path)
time.sleep(5)
start = time.time()
synthesizer.synthesize(text, dirname(__file__) + "/" + text + ".wav")

print "input", text
print "path", path
print "elapsed time", time.time() - start