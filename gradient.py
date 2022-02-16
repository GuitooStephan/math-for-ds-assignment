import numpy as np

x_dim , y_dim = None, None

while ( not x_dim ) :
    try:
        x_dim = float( input('Input the coordinate x: ') )
    except ValueError as e:
        print( 'Try with a numerical value' )

while ( not y_dim ) :
    try:
        y_dim = float( input('Input the coordinate y: ') )
    except ValueError as e:
        print( 'Try with a numerical value' )

gradient = np.array( [ [ 2*x_dim*y_dim - y_dim**2 ], [ x_dim**2 - 2*x_dim*y_dim ] ] )

print( f'The gradient is {gradient}' )