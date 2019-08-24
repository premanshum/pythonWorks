from airtravel import Flight, Aircraft
from pprint import pprint as pp

aa = Aircraft("AD", "AIRBUS", 40, 8)

f = Flight("QA780", aa)

pp(f._seating)

f.allocate_seat('3A', 'Prem')
f.allocate_seat('3B', 'Priya')

pp(f._seating)

f.allocate_seat('3B', 'Alia')