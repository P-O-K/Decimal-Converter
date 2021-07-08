from string import ascii_lowercase as ALS
from string import digits as BDS

def DecimalConverter( x, base=10 ):
	if ( base<2 )|( base>36 ): raise Exception( "Base value must be >= 2 and <= 36" )
	
	if( type( x ) == float ): return int( x );

	HEX_2_BIN = { key:value for value, key in enumerate( ( BDS+ALS )[ :base ] ) }
	TOTAL = 0
	for index, value in enumerate( reversed( str( x ) ) ):
		try: TOTAL += HEX_2_BIN[ value ] *pow( base, index )
		except KeyError as sadFace:
			return False
	return TOTAL
