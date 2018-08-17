# Problem: https://projecteuler.net/problem=102

''' Math Tip:
    Let there be a triangle with 3 points p1=(x_1,y_1),p2=(x_2,y_2) and p3=(x_3,y_3).
    Let p1,p2,p3 be the position vectors.If origin lies within, then cross product of
    any one position vector with other two will be different in sign ( one negative , one positive ).
    But if origin lies outside then there will be one point which has negative 
    cross product with both the other points. So for each point i find points whose
    cross product is less than 0.
    => Link: https://stackoverflow.com/questions/27713046/number-of-triangles-containing-the-point-0-0
'''
def cross_product(vector_a, vector_b):
    return (float(vector_a[0]) * float(vector_b[1])) - (float(vector_a[1]) * float(vector_b[0]))

def triangle_containment():
    includes_origin = 0
    three_co_ordinates_list = [ co_ordinates.split(',') for co_ordinates in open("p102_triangles.txt").read().splitlines() ]
    for three_co_ordinates in three_co_ordinates_list:
        cord_a = three_co_ordinates[0:2]
        cord_b = three_co_ordinates[2:4]
        cord_c = three_co_ordinates[4:6]
        result_1 = cross_product(cord_a, cord_b)
        result_2 = cross_product(cord_a, cord_c)
        if result_1 > 0 and result_2 < 0 or result_1 < 0 and result_2 > 0:
            includes_origin += 1
    return includes_origin

if __name__ == "__main__":
    print("Number of tringales that include origin are: {}".format(triangle_containment()))