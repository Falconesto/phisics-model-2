import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from input import Input
from matrix import Matrix


class Graphic:

    def __init__(self, a, u):
        self.a = a
        self.u = u
        self.click = 0

    def get(self):
        while True:
            cmd = input('Enter "e" to show next iteration or "q" to stop the program: ')
            if cmd == 'e':
                is_similar = self.button()
                if is_similar:
                    print("The temperature graph became linear. The program is terminated.")
                    print("Thank you for using our program. See ya later!")
                    break
            elif cmd == 'q':
                print("Thank you for using our program. See ya later!")
                break
            else:
                print("Invalid command.")

    def button(self):
        is_similar = True
        eps = 0.02
        fig, ax = plt.subplots()
        print("t = " + str(self.click * Input.DELTA_T))
        print(self.u)
        print("--------------------------")

        current_ax_points = []
        current_ay_points = []
        ideal_ax_points = [0, Input.LENGTH]
        ideal_ay_points = [Input.U_0, Input.U_LENGTH]

        #debug_dif = 0
        linear_k = (Input.U_0 - Input.U_LENGTH)/(0 - Input.LENGTH)
        linear_b = Input.U_0

        for i in range(len(self.u)):
            current_x = i * Input.DELTA_X
            current_ax_points.append(current_x)
            current_ay_points.append(self.u[i])
            #if debug_dif < abs(self.u[i] - (linear_k*current_x + linear_b)):
             #   debug_dif = abs(self.u[i] - (linear_k*current_x + linear_b))
            if abs(self.u[i] - (linear_k*current_x + linear_b)) >= eps:
                is_similar = False

        step_x = Input.LENGTH / (len(self.u) - 1)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(step_x))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
        ax.grid()

        plt.plot(current_ax_points, current_ay_points, 'bo-')
        plt.plot(ideal_ax_points, ideal_ay_points, 'r-')
        plt.show()

        self.click += 1

        self.u = Matrix(self.u, self.a).solve()

        return is_similar
