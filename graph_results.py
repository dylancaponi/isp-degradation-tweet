import json

with open('results.log') as f:
    results = [json.loads(line) for line in f]

for line in results:
	print line['download']