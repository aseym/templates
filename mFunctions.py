

# 0 - 9
# 10 19 script main
# 20 script function/class
# 30 OS
# 40 filesystem
# 50 network
# 60 database
# 70 api
# 80 ...
# 90 other remote services
# 100 unknown
#
# -x fatal
# minor to severe

def mFunctionName(k):
    """ Function descrition
        in
        out

    """
    try:

        r = {
            'code':10,
            'message':'Start',
            'result':None

        }
        # do something
        # ask for forgiveness or request permission?
        message = 'passed in %s' % (k)
        print(message)
        r = {
            'code':0,
            'message':'End',
            'result':None

        }
        return r
    except ValueError as error:
        print(error)
        r = {
            'code': 20,
            'message': '',
            'result': None

        }
        return r


k={
    '1':'one',
    '2':'two',
    '3':'three',
}
result = mFunctionName(k)
if result['code'] != 0:
    message = 'Problem with function'
    print(message)
else:
    # All good
    # Store result if there is one for later use.
    pass

