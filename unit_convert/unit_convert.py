# You should be able to use the python interpreter to run this script.
# and it should display 5 test failures. You need to write the code
# for the function so that all of the tests pass.
#
# IMPORTANT:
# Only modify the code where indicated. Do not modify the intent of the test
#


def to_mhz_per_km(band_ghz, r_m, precision=2):
    """Return the result in a fictitious unit of MHz/km.

    band_ghz  : A band string in GHz.
    r_m       : A string representing the range of the link in m(meter).
    precision : <optional> The display precision of the result. 
    
    This function should extract the numeric values, convert the values
    to the appropriate units and then return a string showing the 
    calculated result to the required precision. Don't forget the units.
    
    >>> to_mhz_per_km("3.2 GHz", "3248 m")
    '985.22 MHz/km'
    >>> to_mhz_per_km("4.5 GHz", "124.6 m", 3)
    '36115.570 MHz/km'
    >>> to_mhz_per_km("4.5 GHz", "124.6 m", 0)
    '36116 MHz/km'
    >>> to_mhz_per_km("6.2gHz", "4832.654M", 5)
    '1282.93894 MHz/km'
    >>> to_mhz_per_km("6gHz", "4832M")
    '1241.72 MHz/km'
    
    """
    # MODIFY IN HERE ONLY
    num_chars = ['0','1','2','3','4','5','6','7','8','9','.']
    alph_chars = ['g','G','h','H','z','Z']

    # segregate band value and unit
    band_ghz_value = [x for x in band_ghz if x in num_chars]
    band_ghz_unit = [x.lower() for x in band_ghz if x in alph_chars]

    band_ghz_value = (float)("".join(band_ghz_value))
    band_ghz_unit = "".join(band_ghz_unit)

    # segregate link value and unit
    r_m_value = [x for x in r_m if x in num_chars]
    r_m_unit = [x.lower() for x in r_m if x in alph_chars]

    r_m_value = (float)("".join(r_m_value))
    r_m_unit = "".join(r_m_unit)

    # calculate speed in MHz/km
    mhz_per_km = str(round(band_ghz_value/r_m_value * 1000000,precision))
    speed_split= mhz_per_km.split('.')

    # Check and correct precision to print
    if not precision == 0:
        speed_split[1] = speed_split[1].ljust(precision,'0')
        mhz_per_km = ".".join(speed_split) + ' MHz/km'
    else:
        mhz_per_km = speed_split[0] + ' MHz/km'

    return mhz_per_km
    
    # END MODIFY IN HERE ONLY
 

if __name__ == '__main__':
    import doctest
    doctest.testmod()


