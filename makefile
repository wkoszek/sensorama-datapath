all:
	(cd files && make unpack)
	./tools/sensorama.py schema/sensorama.schema.json files/*.json
	(cd files && make pack)
