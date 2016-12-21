# This program takes two numbers as input, a and b.
#  The greatest common divisor of a and b is calculated through the Euclidean Algorithm.
#  The general solution (x,y) to an equation of the form ax+by=gcd(a,b) is calculated
#  through back substitution.

# take in 2 numbers
first = int(raw_input ("\nFirst number: "))
second = int(raw_input ("Second number: "))

# Special case if either (or both) of the numbers are 0
if first == 0:
    print "The gcd of %s and %s is %s." % (first, second, second)

elif second == 0:
    print "The gcd of %s and %s is %s." % (first, second, first)

else:
    # define absolute value of inputted numbers for EA
    e = abs(first)
    f = abs(second)

    # set default values for EA
    remainders = []
    quotients = []
    bs = [1]
    r = 1
    a = max(e,f)
    b = min(e,f)

    print "\nBy the Euclidean Algorithm, "
    # run and print Euclidean Algorithm
    while r != 0:
        d = divmod(a,b)
        q = d[0]
        r = d[1]
        remainders.append(r)
        quotients.append(q)
        print "\t %s = %s + %s*%s" % (a,r,q,b)
        a = b
        b = r

    # if absolute value of smaller number is gcd 
    if len(remainders) < 2:
        gcd  = min(e,f)
        print "\nTherefore, the gcd of %s and %s is %s." % (first, second, gcd)
        if e > f:
            print "The general solution to %s*x + %s*y = gcd(%s,%s) = %s is" % (first, second, first, second, gcd)
            print "\n\t(x,y) = (0,%s) + k(%s,%s) for an integer k." % (second/f,-second/gcd,first/gcd)
        else:
            print "The general solution to %s*x + %s*y = gcd(%s,%s) = %s is" % (first, second, first, second, gcd)
            print "\n\t(x,y) = (%s,0) + k(%s,%s) for an integer k." % (first/e,-second/gcd,first/gcd)

    #otherwise, back substitution is used
    else:
        # gcd is second last remainder, or last divisor
        gcd = remainders[-2]

        print "\nTherefore, the gcd of %s and %s is %s." % (first, second, gcd)

        # set up for back substitution
        bs.append(quotients[-2]*-1)

        # produce sequence for back substitution in bs
        for i in range(len(quotients)-3, -1, -1):
            bs.append(bs[-2]-quotients[i]*bs[-1])

        # determine order of variables in equation
        if e>f:
            order = -2
        else:
            order = -1

        # one solution to the equation ax+by = gcd(a,b)
        x1 = bs[order]*first/e
        y1 = bs[2/order]*second/f
        
        print "By Back Substitution, we have %s*%s + %s*%s = %s = %s.\n" % (first,x1,second,y1,first*x1+second*y1, gcd)
        print "The general solution to %s*x + %s*y = gcd(%s,%s) = %s is" % (first, second, first, second, gcd)
        print "\n\t(x,y) = (%s,%s) + k(%s,%s) for an integer k." % (x1,y1,-second/gcd,first/gcd)
