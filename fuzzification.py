class ChestPain:
    def __int__(self):
        pass

    def typical_anginal(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def atypical_anginal(self, x):
        if x == 2:
            return 1
        else:
            return 0

    def non_angial_pain(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def asymptomatic(self, x):
        if x == 4:
            return 1
        else:
            return 0

    def fuzzify(self, cp):
        res = {
            'typical_anginal': self.typical_anginal(cp),
            'atypical_anginal':self.atypical_anginal(cp),
            'non_anginal_pain': self.non_angial_pain(cp),
            'asymptomatic': self.asymptomatic(cp)
        }
        return res

class BloodPressure:
    def __init__(self):
        pass

    def bloodPressure_low(self, x):
        if x <= 111:
            return 1
        if 111 < x <= 134:
            return (-x + 134) / 23
        else:
            return 0

    def bloodPressure_medium(self, x):
        if 127 < x <= 139:
            return (x - 127) / 12
        if 139 < x < 153:
            return (-x + 153) / 14
        else:
            return 0

    def bloodPressure_high(self, x):
        if 142 < x <= 157:
            return (x - 142) / 15
        if 157 < x <= 172:
            return (-x + 172) / 15
        else:
            return 0

    def bloodPressure_veryhigh(self, x):
        if 154 < x < 171:
            return (x - 154) / 17
        if 171 <= x:
            return 1
        else:
            return 0

    def fuzzify(self, bp):
        res = {
            'low':self.bloodPressure_low(bp),
            'medium':self.bloodPressure_medium(bp),
            'high':self.bloodPressure_high(bp),
            'very_high':self.bloodPressure_veryhigh(bp)
        }
        return res

class Cholesterol:
    def __init__(self):
        pass

    def cholesterol_low(self, x):
        if x <= 151:
            return 1
        if 151 < x <= 197:
            return (-x + 197) / 46
        else:
            return 0

    def cholesterol_medium(self, x):
        if 188 < x <= 215:
            return (x - 215) / 27
        if 215 < x <= 250:
            return (-x + 250) / 35
        else:
            return 0

    def cholesterol_high(self, x):
        if 217 < x <= 263:
            return (x - 217) / 46
        if 307 < x <= 263:
            return (-x + 307) / 44
        else:
            return 0

    def cholesterol_veryhigh(self, x):
        if 281 < x <= 347:
            return (x - 281) / 66
        if 347 <= x:
            return 1
        else:
            return 0

    def fuzzify(self, ch):
        res = {
            'low': self.cholesterol_low(ch),
            'medium': self.cholesterol_medium(ch),
            'high': self.cholesterol_high(ch),
            'very_high': self.cholesterol_veryhigh(ch)
        }
        return res


class BloodSugar:
    def __init__(self):
        pass

    def bloodSugar_veryhigh(self, x):
        if x <= 105:
            return 0
        if 105 < x < 120:
            return (x - 105) / 15
        else:
            return 1

    def fuzzify(self, bs):
        res = {
            'true': self.bloodSugar_veryhigh(bs),
            'false': 1 - self.bloodSugar_veryhigh(bs)
        }
        return res

class ECG:
    def __init__(self):
        pass

    def ECG_normal(self, x):
        if x <= 0:
            return 1
        if 0 < x <= 0.4:
            return (-x + 0.4) / 0.4
        else:
            return 0

    def ECG_abnormal(self, x):
        if 0.2 < x <= 1:
            return (x - 0.2) / 0.8
        if 1 < x <= 1.8:
            return (-x + 1.8) / 0.8
        else:
            return 0

    def ECG_hypertrophy(self, x):
        if 1.4 < x <= 1.9:
            return (x - 1.4) / 0.5
        if 1.9 <= x:
            return 1
        else:
            return 0

    def fuzzify(self, ecg):
        res = {
            'normal': self.ECG_normal(ecg),
            'abnormal': self.ECG_abnormal(ecg),
            'hypertrophy': self.ECG_hypertrophy(ecg)
        }
        return res

class HeartRate:
    def __init__(self):
        pass

    def heartRate_low(self, x):
        if x <= 100:
            return 1
        if 100 < x <= 141:
            return (-x + 141) / 41
        else:
            return 0

    def heartRate_medium(self, x):
        if 111 < x <= 152:
            return (x - 111) / 41
        if 152 < x <= 194:
            return (-x + 194) / 42
        else:
            return 0

    def heartRate_high(self, x):
        if 152 < x < 210:
            return (x - 152) / 58
        if 210 <= x:
            return 1
        else:
            return 0

    def fuzzify(self, hr):
        res = {
            'low': self.heartRate_low(hr),
            'medium': self.heartRate_medium(hr),
            'high': self.heartRate_high(hr)
        }
        return res

class Exercise:
    def __init__(self):
        pass

    def no_problem(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def dangerous(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def fuzzify(self, ex):
        res = {
            'true': self.no_problem(ex),
            'false': self.dangerous(ex)
        }
        return res
class OldPeak:
    def __init__(self):
        pass

    def oldPeak_low(self, x):
        if x <= 1:
            return 1
        if 1 < x <= 2:
            return (-x + 2) / 1
        else:
            return 0

    def oldPeak_risk(self, x):
        if 1.5 < x <= 2.8:
            return (x - 1.5) / 1.3
        if 2.8 < x <= 4.2:
            return (-x + 4.2) / 1.4
        else:
            return 0

    def oldPeak_terrible(self, x):
        if 2.5 < x <= 4:
            return (x - 2.5) / 1.5
        if 4 <= x:
            return 1
        else:
            return 0

    def fuzzify(self, op):
        res = {
            'low': self.oldPeak_low(op),
            'risk': self.oldPeak_risk(op),
            'terrible': self.oldPeak_terrible(op)
        }
        return res


class Thallium:
    def __init__(self):
        pass

    def normal(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def medium(self, x):
        if x == 6:
            return 1
        else:
            return 0

    def high(self, x):
        if x == 7:
            return 1
        else:
            return 0

    def fuzzify(self, th):
        res = {
            'normal': self.normal(th),
            'medium': self.medium(th),
            'high': self.high(th)
        }
        return res

class Sex:
    def __init__(self):
        pass

    def female(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def male(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def fuzzify(self, s):
        res = {
            'male': self.male(s),
            'female': self.female(s)
        }
        return res

class Age:
    def __init__(self):
        pass

    def age_young(self, x):
        if x < 29:
            return 1
        if 29 <= x <= 38:
            return (-x + 38) / 9
        if x > 38:
            return 0

    def age_mild(self, x):
        if x < 33:
            return 0
        if 33 <= x <= 38:
            return (x - 33) / 5
        if 38 < x <= 45:
            return (-x + 45) / 7
        if x > 45:
            return 0

    def age_old(self, x):
        if x < 40:
            return 0
        if 40 <= x <= 48:
            return (x - 40) / 8
        if 48 < x < 58:
            return (-x + 58) / 10
        else:
            return 0

    def age_veryold(self, x):
        if x < 52:
            return 0
        if 52 <= x <= 60:
            return (x - 52) / 8
        if 60 <= x:
            return 1

    def fuzzify(self, age):
        res = {
            'young': self.age_young(age),
            'mild': self.age_mild(age),
            'old': self.age_old(age),
            'very_old': self.age_veryold(age)
        }
        return res

class Output:
    def __int__(self):
        pass

    def healthy(self, x):
        if x <= 0.25:
            return 1
        if 0.25 < x <= 1:
            return (-x + 1) / 0.75
        else:
            return 0

    def output_sick1(self, x):
        if 0 < x <= 1:
            return x
        if 1 < x <= 2:
            return -x + 2
        else:
            return 0

    def output_sick2(self, x):
        if 1 < x <= 2:
            return x - 1
        if 2 < x <= 3:
            return -x + 3
        else:
            return 0

    def output_sick3(self, x):
        if 2 < x <= 3:
            return x - 2
        if 3 < x <= 4:
            return -x + 4
        else:
            return 0

    def output_sick4(self, x):
        if 3 < x <= 3.75:
            return (x-3) / 0.75
        if 3.75 <= x:
            return 1
        else:
            return 0


class Fuzzify:
    def __int__(self):
        pass

    def fuzzification_output(self, input):

        chest_pain = ChestPain().fuzzify(float(input['chest_pain']))
        blood_pressure = BloodPressure().fuzzify(float(input['blood_pressure']))
        cholesterol = Cholesterol().fuzzify(float(input['cholestrol']))
        blood_sugar = BloodSugar().fuzzify(float(input['blood_sugar']))
        ecg = ECG().fuzzify(float(input['ecg']))
        heart_rate = HeartRate().fuzzify(float(input['heart_rate']))
        exercise = Exercise().fuzzify(int(input['exercise']))
        old_peak = OldPeak().fuzzify(float(input['old_peak']))
        thallium = Thallium().fuzzify(float(input['thallium_scan']))
        sex = Sex().fuzzify(int(input['sex']))
        age = Age().fuzzify(float(input['age']))

        return chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, exercise, old_peak, thallium, sex, age
