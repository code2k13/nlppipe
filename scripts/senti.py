from afinn import Afinn
import sys
import json

afinn = Afinn()
for line in sys.stdin:
    obj  = json.loads(line)
    score = afinn.score(obj["tweet"])
    obj["afinn_score"] = score
    print(json.dumps(obj))