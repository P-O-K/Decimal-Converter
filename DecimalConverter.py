
from string import ascii_lowercase as ALS
from string import digits


def DecimalConverter( sequence:type, base:int=10 ) -> int:
	if ( base <2 )|( base >36 ): raise Exception( "Base value must be >= 2 and <= 36" )

	HEX_2_BIN = { key:value for value, key in enumerate( ( digits +ALS )[ :base ] ) }
	TOTAL = 0
	for index, value in enumerate( reversed( str( sequence ) ) ):
		try: TOTAL += HEX_2_BIN[ value ] *pow( base, index )
		except KeyError as sadFace:
			return False
	return TOTAL



if __name__ == '__main__':
	print( DecimalConverter( sequence =  42,      base=10 ) )
	print( DecimalConverter( sequence = '2a',     base=16 ) )
	print( DecimalConverter( sequence = '16',     base=36 ) )
	print( DecimalConverter( sequence = '101010', base=2 ) )
