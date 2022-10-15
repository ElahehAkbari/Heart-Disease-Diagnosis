from fuzzification import Fuzzify
from inference import FuzzyInference
from defuzzification import Defuzzify

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        # print("input_dict ", input_dict)
        fuzz_res = Fuzzify()
        inference_res = FuzzyInference()
        defuzz_res = Defuzzify()

        chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, exercise, old_peak, thallium, sex, age = fuzz_res.fuzzification_output(input_dict)

        fuzzy_sickness = inference_res.inference_result(chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, exercise, old_peak, thallium, sex, age)

        return defuzz_res.defuzzify(fuzzy_sickness)