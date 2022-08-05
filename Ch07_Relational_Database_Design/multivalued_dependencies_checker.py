from typing import List, Set, Tuple

def tuple_over_set_equality_checker(t1: Tuple, t2: Tuple, t3: Tuple, t4: Tuple, s: Set[int]) -> bool:
    for i in s:
        if not (t1[i] == t2[i] == t3[i] == t4[i]):
            return False
    return True

class Solution: 
    def __init__(self, doesTheMultivaluedDependencyHold=True, t1=tuple(), t2=tuple()): 
        '''
        t1 and t2 are only meaningful if the parameter 
        doesTheMultivaluedDependencyHold is False. That is 
        if the multivalued dependency does not hold, then t1 and 
        t2 represent tuples in the instance of the relation that don't 
        have corresponding t3 and t4 to satisfy the definition of the 
        multivalued dependency.  
        '''
        self.doesTheMultivaluedDependencyHold = doesTheMultivaluedDependencyHold
        self.t1 = t1
        self.t2 = t2
    
    def __str__(self): 
        if self.doesTheMultivaluedDependencyHold: 
            return 'Multivalued Dependency holds!! 👍👍'
        else: 
            return 'Multivalued Dependency does NOT hold 😥😔\n' \
            'Problem causing tuples are \n\t t1: {} \n\t t2: {}'.format(self.t1, self.t2)
        
def multivalued_dependency_checker(r: List[Tuple], R: Set[int], alpha: Set[int], beta: Set[int]) -> bool:
    '''
    r: is the instance of the relation. It is basically 
    a list of the tuples, where each tuple represents 
    a row inside of the relation. 

    R: the schema. Is the set of integers to indicate the attributes. 
    It usually includes numbers from 0 upto n, where n is 
    some natural number.

    We are testing the multivalued dependency alpha ->-> beta.
    alpha and beta are subsets of R. 
    '''
    R_minus_beta = R - beta
    number_of_attributes = len(r[0])

    for i in range(0, len(r)):
        for j in range(i+1, len(r)):
            t1 = r[i]
            t2 = r[j]

            # build t3
            t3 = [0] * number_of_attributes

            # since t3[beta] is equal to t1[beta]
            for k in beta:
                t3[k] = t1[k]

            # also t3[R - beta] = t2[R - beta]
            for k in R_minus_beta:
                t3[k] = t2[k]

            # build t4
            t4 = [0] * number_of_attributes

            # since t4[beta] is equal to t2[beta]
            for k in beta:
                t4[k] = t2[k]
            
            # since t4[R - beta] is equal to t1[R - beta]
            for k in R_minus_beta:
                t4[k] = t1[k]
            
            if (not tuple_over_set_equality_checker(t1, t2, t3, t4, alpha)): 
                return Solution(False, t1, t2)
            
            t3 = tuple(t3)
            t4 = tuple(t4)
            
            if (t3 in r) and (t4 in r): 
                # all is good
                pass 
            else: 
                return Solution(False, t1, t2)
    return Solution(True)


if __name__ == '__main__':
    print(multivalued_dependency_checker(
        [
            (1, 3, 7, 2),
            (1, 6, 4, 5),
            (1, 3, 7, 5),
            (1, 6, 4, 2),
        ], # the relation
        {0, 1, 2, 3}, # the schema
        {0,}, # alpha
        {1,2},# beta
    ))
