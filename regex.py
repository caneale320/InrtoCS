# Caleb Neale, can4ku

import re

nospace = re.compile(r"(\S)+")

quotation = re.compile(r"^\"[^\s\"]?[^\"]*")

twonum = re.compile(r"(\-?\d+\.?\d*\s/-?\d+\.?\d*)|(\-?\d+\.?\d*(,)\-?\d+\.?\d*)|(\-?\d+\.?\d*(,)( )\-?\d+\.?\d*)|(\-?\d+\.?\d*( )(,)\-?\d+\.?\d*)")





