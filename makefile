# Copyright (c) 2015, Wojciech A. Koszek
# All rights reserved.
all:
	(cd files && make unpack)
	./tools/sensorama.py schema/sensorama.schema.json files/*.json
	(cd files && make pack)
