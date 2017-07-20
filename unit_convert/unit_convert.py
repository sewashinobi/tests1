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
    st = ''
    for ch in band_ghz:
        try:
            int(ch)
        except:
            pass
        else:
            st += ch
        if ch == '.':
            st += ch

    band_ghz = float(st)
    band_mhz = band_ghz * 1000
    st = ''
    for ch in r_m:
        try:
            int(ch)
        except:
            pass
        else:
            st += ch
        if ch == '.':
            st += ch
    r_m = float(st)
    r_km = r_m / 1000

    result = band_mhz/r_km
    res = round(result, precision)
    if precision == 0:
        res = int(res)
    res = str(res)
    if len(res.split('.')[-1]) < precision:
        for _ in xrange(precision - len(res.split('.')[-1])):
            res += '0'
    return res + ' MHz/km'
    # END MODIFY IN HERE ONLY
 

if __name__ == '__main__':

    import doctest
    doctest.testmod()


