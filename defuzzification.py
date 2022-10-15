from fuzzification import Output

class Defuzzify:
    def __int__(self):
        pass

    def defuzzify(self, input):
        output = Output()
        line = []
        step = 2. / 1000
        for i in range(1001):
            line.append(i * step)

        first_sig = 0.
        second_sig = 0.

        res1 = input['sick_1']
        res2 = input['sick_2']
        res3 = input['sick_3']
        res4 = input['sick_4']
        res_healthy = input['healthy']


        for p in line:
            mem_sick1 = output.output_sick1(p)
            mem_sick2 = output.output_sick2(p)
            mem_sick3 = output.output_sick3(p)
            mem_sick4 = output.output_sick4(p)
            mem_healthy = output.healthy(p)

            if res1 < mem_sick1:
                line_sick1 = res1
            else:
                line_sick1 = mem_sick1

            if res2 < mem_sick2:
                line_sick2 = res2
            else:
                line_sick2 = mem_sick2

            if res3 < mem_sick3:
                line_sick3 = res3
            else:
                line_sick3 = mem_sick3

            if res4 < mem_sick4:
                line_sick4 = res1
            else:
                line_sick4 = mem_sick4

            if res_healthy < mem_healthy:
                line_healthy = res_healthy
            else:
                line_healthy = mem_healthy

            final = max(line_sick1, line_sick2, line_sick3, line_sick4, line_healthy)

            first_sig = first_sig + (final * p)
            second_sig += final

        if second_sig == 0:
            z_star = 0
        else:
            z_star = first_sig/second_sig

        if z_star < 1.78:
            return 'Healthy'
        if 1 <= z_star < 2.51:
            return 'Sick(s1)'
        if 1.78 <= z_star < 3.25:
            return 'Sick(s2)'
        if 1.5 <= z_star < 4.5:
            return 'Sick(s3)'
        if z_star >= 3.25:
            return 'Sick(s4)'

