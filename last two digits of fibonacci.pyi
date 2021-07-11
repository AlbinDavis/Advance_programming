def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = (v2*v2) % 100
        v1, v2, v3 = (v1*v1+calc) % 100, ((v1+v3)*v2) % 100, (calc+v3*v3) % 100
        if rec == '1':
            v1, v2, v3 = (v1+v2) % 100, v1, v2
    return v2
  
  #last one digit of fibonacci number
  
  def fib_last_digit(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = (v2*v2) % 10
        v1, v2, v3 = (v1*v1+calc) % 10, ((v1+v3)*v2) % 10, (calc+v3*v3) % 10
        if rec == '1': v1, v2, v3 = (v1+v2) % 10, v1, v2
    return v2
  
  #based on the concept described in Eugene Yarmash's answer 
  #(the last digits repeat every 60 steps) we can make an even faster solution (O(1)):

def fib_last_digit(n):
    return (
        [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
        [n % 60 - 1]
    )
