all:
	(cd files && make unpack)
	./tools/sensorama.py files/*.json
	(cd files && make pack)
