from math import sin, cos, pi, sqrt, acos, asin, isclose, radians, degrees

# ---------- Helper functions -------------------------------------- #

def aaas(D, E, F, f):
    """ This function solves the triangle and returns (d,e,f,D,E,F) """
    d = f * sin(D) / sin(F)
    e = f * sin(E) / sin(F)
    return (d,e,f,D,E,F)

def sss(d,e,f):
    """ This function solves the triangle and returns (d,e,f,D,E,F) """
    assert d + e > f and e + f > d and f + d > e
    F = acos((d**2 + e**2 - f**2) / (2 * d * e))
    E = acos((d**2 + f**2 - e**2) / (2 * d * f))
    D = pi - F - E
    return (d,e,f,D,E,F)

def sas(d,e,F):
    """ This function solves the triangle and returns (d,e,f,D,E,F) """
    f = sqrt(d**2 + e**2 - 2 * d * e * cos(F))
    return sss(d,e,f)


def ssa(d, e, D, ssa_flag):
    """ This function solves the triangle and returns (d,e,f,D,E,F)
    See docstring for calculate_triangle for definition of ssa_flag"""
    assert ssa_flag in ('acute', 'obtuse', 'forbid'), 'Invalid value of ssa_flag'
    sinE = sin(D) * e / d

    # This whole part is to calculate E
    if isclose(sinE, 1):
        # Right triangle, where the solution is unique
        E = pi/2
    else:
        assert sinE < 1, 'No such triangle'
        E_acute = asin(sinE)
        E_obtuse = pi - E_acute
        acute_is_valid = (0 < (pi - D - E_acute) < pi)
        obtuse_is_valid = (0 < (pi - D - E_obtuse) < pi)

        if ssa_flag == 'acute':
            assert acute_is_valid, 'No such triangle'
            E = E_acute
        elif ssa_flag == 'obtuse':
            assert obtuse_is_valid, 'No such triangle'
            E = E_obtuse
        else:
            assert ssa_flag == 'forbid'
            if acute_is_valid and obtuse_is_valid:
                raise ValueError('Two different triangles fit this description')
            if (not acute_is_valid) and (not obtuse_is_valid):
                raise ValueError('No such triangle')
            E = E_acute if acute_is_valid else E_obtuse
    # Now that we know E, the rest is straightforward
    F = pi - D - E
    e,f,d,E,F,D = aaas(E,F,D,d)
    return (d,e,f,D,E,F)

#area
def area_cal(d,e,f):     
    # Calculate the semi-perimeter
    s = (d + e + f) / 2

    # Calculate the area using Heron's formula
    area = sqrt(s * (s - d) * (s - e) * (s - f))
    return area

#perimeter
def perimeter_cal(d,e,f):
    # Calculate the diameter of the circumscribed circle
    perimeter = d + e + f
    return perimeter


# ---------- Main function -------------------------------------------- #

def calculate_triangle(a, b, c, A, B, C, ssa_flag='forbid'):
    """
    Solve to find all the information about a triangle, given partial
    information.

    a, b, c, A, B, C are the three sides and angles. (e.g. A is the angle
    opposite the side of length a.) Out of these six possibilities, you need
    to tell the program exactly three. Then the program will tell you all six.

    It returns a tuple (a, b, c, A, B, C).

    "ssa" is the situation when you give two sides and an angle which is not
    between them. This is usually not enough information to specify a unique
    triangle. Usually there are two possible triangles—except for a special
    case with right triangles where the two possible triangles are the same
    (the equation has a "double root"), and some cases where one of the two
    possible triangles has a negative angle.

    Therefore there is an 'ssa_flag'. You can set it to'forbid' (raise an error
    if the answer is not unique - the default setting), or 'acute' (where the
    unknown angle across from the known side is chosen to be acute) or 'obtuse'
    (similarly).
    """
    #check for only 3 inputs
    if sum(x is not None for x in (a,b,c,A,B,C)) != 3:
        raise ValueError('Must provide exactly 3 inputs')
    # check for atlest one side
    if sum(x is None for x in (a,b,c)) == 3:
        raise ValueError('Must provide at least 1 side length')
    # check that positive input is entered
    assert all(x > 0 for x in (a,b,c,A,B,C) if x is not None)
    # check that angles dont go over 180 degrees
    assert all(x < pi for x in (A,B,C) if x is not None)
    assert ssa_flag in ('forbid', 'acute', 'obtuse')

    # duplicate data to dict
    known_sides = {'a': a, 'b': b, 'c': c}
    known_angles = {'A': A, 'B': B, 'C': C}

    # 3 side case
    if sum(x is not None for x in known_sides.values()) == 3:
        a, b, c, A, B, C = sss(a, b, c)
    
    # 2 side case
    elif sum(x is not None for x in known_sides.values()) == 2:
        for side1, side2, angle in [('a', 'b', 'C'), ('b', 'c', 'A'), ('c', 'a', 'B')]:
            if known_sides[side1] is not None and known_sides[side2] is not None and known_angles[angle] is not None:
                a, b, c, A, B, C = sas(known_sides[side1], known_sides[side2], known_angles[angle])
                break
        else:
            for side1, angle, side2 in [('a', 'A', 'b'), ('a', 'A', 'c'), ('b', 'B', 'a'), ('b', 'B', 'c'), ('c', 'C', 'a'), ('c', 'C', 'b')]:
                if known_sides[side1] is not None and known_angles[angle] is not None and known_sides[side2] is not None:
                    a, b, c, A, B, C = ssa(known_sides[side1], known_sides[side2], known_angles[angle], ssa_flag)
                    break
    elif sum(x is not None for x in known_sides.values()) == 1:
        # Find the third angle...
        if A is None:
            A = pi - B - C
        elif B is None:
            B = pi - A - C
        else:
            C = pi - A - B

        #ceck that value of atlest one side > 0
        assert A > 0 and B > 0 and C > 0
        # Then solve the triangle...
        if c is not None:
            a,b,c,A,B,C = aaas(A,B,C,c)
        elif a is not None:
            b,c,a,B,C,A = aaas(B,C,A,a)
        else:
            c,a,b,C,A,B = aaas(C,A,B,b)

    # area
    a = area_cal(a,b,c)
    #perimeter
    p = perimeter_cal(a,b,c)

    return (a,b,c,A,B,C,a,p)




# # -----LOCAL TEST------
# angle2 = radians(60)
# print(angle2)
# result = (calculate_triangle(a=5, b=5, c=None, A=None, B= angle2, C=None))

# #angle1 = A ,angle2 = B ,angle3 = C : side1  = c ,side2  = b ,side3  = a 

# side3 = result[0]
# side2  = result[1]
# side1 = result[2]
# angle1 = (result[3])
# angle2 = (result[4])
# angle3 = (result[5])
# area = (result[6])
# perimeter = (result[7])

# print(f"angle1 = {angle1} ,angle2 = {angle2} ,angle3 = {angle3} : side1  = {side1} ,side2  = {side2} ,side3  = {side3}, area = {area}, perimeter = {perimeter}")