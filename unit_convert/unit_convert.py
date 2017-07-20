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
    import re
    numerator = eval(re.findall('([\d.]*)', band_ghz)[0])*1000*1000
    denominator = eval(re.findall('([\d.]*)', r_m)[0])
    if precision == 0:
        precision2 = 2
    else:
        precision2 = precision
    output1 = str(round(round(numerator, precision2)/round(denominator, precision2), precision))
    output1 += '0'*precision
    output2 = output1[0: output1.find('.')+(precision+1 if precision != 0 else precision)]
    output3 = str(output2)+' MHz/km'
    return output3

    # END MODIFY IN HERE ONLY
 

if __name__ == '__main__':
    import doctest
    doctest.testmod()