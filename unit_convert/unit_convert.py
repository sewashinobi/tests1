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
    r_m       : A string representing the range of the link in m.
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

    # strip the units
    band_ghz = band_ghz.lower().strip('ghz').strip(' ')
    r_k = r_m.lower().strip('m').strip(' ')

    #  make its a float if it's not
    if '.' not in band_ghz:
        band_ghz += '.0'
    if '.' not in r_k:
        r_k += '.0'

    # convert units
    band_mhz = float(band_ghz)*1000.0
    r_km = float(r_k)/1000.0

    return "%0.*f MHz/km" % (precision, band_mhz/ r_km)
    
    # END MODIFY IN HERE ONLY
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()


