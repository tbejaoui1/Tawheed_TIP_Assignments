#input, n, was initially the index of the fibonacci sequence
#Output should be the expected result of that index within the fibonacci series
# However, calling the function for terms higher than and equal to 2 prove to be difficult
#since the previous values had to be known and stored in memory. Thus, a while and count method
#had to be used.

nterms = int(input("How many terms? "))
#base cases:
#f0 = 1
#f1= 1
# "(n-1) + (n-2)" b/c Fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21....

def Rec_Fib(nterms):
    #base cases:
    if nterms == 0:
        return 1
    if nterms == 1:
        return 1
    #Establishing a Recursive Soln: [need to call the function again and again to solve the next, but requires base]
    # this return statement takes you outside of the fcn/if conditions and uses those base cases
    return Rec_Fib(nterms - 1) + Rec_Fib(nterms - 2)

result = Rec_Fib(nterms)
print(result)






# Turns out the below code wasn't using recursive technique since a while loop had to be used.....recursive solution
# is a substitute for an iterative soln (like: while and for loops. 
# def fib(nterms):
#     count = 0
#     if nterms < 0:
#         print("please use only positive integers, 0 and up")
#     if nterms == 0 or nterms == 1:
#         print(nterms)
#
#
#     else:
#         if nterms == 2:
#             n0 = 0
#             n1 = 1      #tried fib(0) and fib(1) but gave me an error stating that it doesn't support the object type when +
#             nth = n0 + n1
#             print(nth)
#
#
#
#         if nterms > 2:
#             while count < nterms:
#                 #previously computed
#                 print(n0)
#                 print(n1)
#                 # need to be updating the n terms wrt nterm input
#                 nth = n0 + n1
#                 print(nth)
#                 # updating for the next count
#                 n0 = n1
#                 n1 = nth
#                 count =+ 1
#
# #since a function has been defined, it must be called in order for it to work.
# fib(nterms)




