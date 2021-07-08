from string import ascii_lowercase as ALS
from string import digits as BDS

def DecimalConverter( string, base=10 ):
	if (base<2) | (base>36): raise Exception( "ValueError: int() base must be >= 2 and <= 36, or 0" )

	HEX_2_BIN = { key:value for value,key in enumerate( ( BDS+ALS )[ :base ] ) }
	TOTAL = 0
	for index,value in enumerate( reversed( string ) ):
		try:
			TOTAL += HEX_2_BIN[ value ] *pow( base, index )
		except KeyError as sadFace:
			return False
	return TOTAL
