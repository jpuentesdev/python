#https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python
def nb_year(p0, percent, aug, p):
    current_pop = p0
    year = 0
    while current_pop < p:
        current_pop = int(current_pop + (percent / 100 * current_pop) + aug)
        year +=1
    return year
        
