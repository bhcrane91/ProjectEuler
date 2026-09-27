conv = lambda x: [int(i) for i in x.split(",")]
triangles = [conv(line) for line in open("triangles.txt","r").read().split("\n")]

# https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Conversion_between_barycentric_and_Cartesian_coordinates

between = lambda x: 0 < x and x < 1
x,y = 0,0
S = 0 
for triangle in triangles:
    x1, y1, x2, y2, x3, y3 = triangle
    det_t = ((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3))
    lambda_1 = ((y2-y3)*(x-x3)+(x3-x2)*(y-y3)) / det_t 
    lambda_2 = ((y3-y1)*(x-x3)+(x1-x3)*(y-y3)) / det_t
    lambda_3 = 1 - lambda_1 - lambda_2
    S += (between(lambda_1) and between(lambda_2) and between(lambda_3))
print(S)