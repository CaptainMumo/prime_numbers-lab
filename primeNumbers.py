def primeNumbers(number):
    return [x for x in range(2,number + 1) if all(x%y != 0 for y in range(2,x))]

    """prime_numbers = [2]

    if number <= 1:
        return []
    else:   
        for x in range(2, number+1):
            for y in range(2,x):
                if x%y == 0: 
                    break
                else:   
                    prime_numbers.append(x)
                    break           
        return prime_numbers """           

