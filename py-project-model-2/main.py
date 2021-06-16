from graphic import Graphic
import initial_distribution

if __name__ == '__main__':
    a = float(input("Enter the heat coefficient value: "))
    initial_u = initial_distribution.get()
    Graphic(a, initial_u).get()
