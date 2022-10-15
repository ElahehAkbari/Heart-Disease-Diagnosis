class FuzzyInference:
    def __int__(self):
        pass

    def inference_result(self, chest_pain, blood_pressure, cholesterol,
                         blood_sugar, ecg, heart_rate, exercise, old_peak,
                         thallium, sex, age):

        # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
        m1_sick4 = min(float(age['very_old']), float(chest_pain['atypical_anginal']))

        # RULE 2: IF (heart_rate IS high) AND (age IS old) THEN health IS sick_4;
        m2_sick4 = min(float(heart_rate['high']), float(age['old']))

        # RULE 3: IF (sex IS male) AND (heart_rate IS medium) THEN health IS sick_3;
        m1_sick3 = min(float(sex['male']), float(heart_rate['medium']))

        # RULE 4: IF (sex IS female) AND (heart_rate IS medium) THEN health IS sick_2;
        m1_sick2 = min(float(sex['female']), float(heart_rate['medium']))

        # RULE 5: IF (chest_pain IS non_anginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
        m2_sick3 = min(float(chest_pain['non_anginal_pain']), float(blood_pressure['high']))

        # RULE 6: IF (chest_pain IS typical_anginal) AND (heart_rate IS medium) THEN health IS sick_2;
        m2_sick2 = min(float(chest_pain['typical_anginal']), float(heart_rate['medium']))

        # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
        m3_sick3 = min(float(blood_sugar['true']), float(age['mild']))

        # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
        m3_sick2 = min(float(blood_sugar['false']), float(blood_pressure['very_high']))

        # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
        m1_sick1 = max(float(chest_pain['asymptomatic']), float(age['very_old']))

        # RULE 10: IF (blood_pressure IS high) OR (heart_rate IS low) THEN health IS sick_1;
        m2_sick1 = max(float(blood_pressure['high']), float(age['very_old']))

        # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
        m1_healthy = float(chest_pain['typical_anginal'])

        # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
        m3_sick1 = float(chest_pain['atypical_anginal'])

        # RULE 13: IF (chest_pain IS non_anginal_pain) THEN health IS sick_2;
        m4_sick2 = float(chest_pain['non_anginal_pain'])

        # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
        m4_sick3 = float(chest_pain['asymptomatic'])

        # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
        m3_sick4 = float(chest_pain['asymptomatic'])

        # RULE 16: IF (sex IS female) THEN health IS sick_1;
        m4_sick1 = float(sex['female'])

        # RULE 17: IF (sex IS male) THEN health IS sick_2;
        m5_sick2 = float(sex['male'])

        # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
        m2_healthy = float(blood_pressure['low'])

        # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
        m5_sick1 = float(blood_pressure['medium'])

        # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
        m6_sick2 = float(blood_pressure['high'])

        # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
        m5_sick3 = float(blood_pressure['high'])

        # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
        m4_sick4 = float(blood_pressure['very_high'])

        # RULE 23: IF (cholestrol IS low) THEN health IS healthy;
        m3_healthy = float(cholesterol['low'])

        # RULE 24: IF (cholestrol IS medium) THEN health IS sick_1;
        m6_sick1 = float(cholesterol['medium'])

        # RULE 25: IF (cholestrol IS high) THEN health IS sick_2;
        m7_sick2 = float(cholesterol['high'])

        # RULE 26: IF (cholestrol IS high) THEN health IS sick_3;
        m6_sick3 = float(cholesterol['high'])

        # RULE 27: IF (cholestrol IS very_high) THEN health IS sick_4;
        m5_sick4 = float(cholesterol['very_high'])

        # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
        m8_sick2 = float(blood_sugar['true'])

        # RULE 29: IF (ecg IS normal) THEN health IS healthy;
        m4_healthy = float(ecg['normal'])

        # RULE 30: IF (ecg IS normal) THEN health IS sick_1;
        m7_sick1 = float(ecg['normal'])

        # RULE 31: IF (ecg IS abnormal) THEN health IS sick_2;
        m9_sick2 = float(ecg['abnormal'])

        # RULE 32: IF (ecg IS hypertrophy) THEN health IS sick_3;
        m7_sick3 = float(ecg['hypertrophy'])

        # RULE 33: IF (ecg IS hypertrophy) THEN health IS sick_4;
        m6_sick4 = float(ecg['hypertrophy'])

        # RULE 34: IF (heart_rate IS low) THEN health IS healthy;
        m5_healthy = float(heart_rate['low'])

        # RULE 35: IF (heart_rate IS medium) THEN health IS sick_1;
        m8_sick1 = float(heart_rate['medium'])

        # RULE 36: IF (heart_rate IS medium) THEN health IS sick_2;
        m10_sick2 = float(heart_rate['medium'])

        # RULE 37: IF(heart_rate IS high) THEN health IS sick_3;
        m8_sick3 = float(heart_rate['high'])

        # RULE 38: IF(heart_rate IS high) THEN health IS sick_4;
        m7_sick4 = float(heart_rate['high'])

        # RULE 39: IF (exercise IS true) THEN health IS sick_2;
        m11_sick2 = float(exercise['true'])

        # RULE 40: IF (old_peak IS low) THEN health IS healthy;
        m6_healthy = float(old_peak['low'])

        # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
        m9_sick1 = float(old_peak['low'])

        # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
        m12_sick2 = float(old_peak['terrible'])

        # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
        m9_sick3 = float(old_peak['terrible'])

        # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
        m8_sick4 = float(old_peak['risk'])

        # RULE 45: IF (thallium_scan IS normal) THEN health IS healthy;
        m7_healthy = float(thallium['normal'])

        # RULE 46: IF (thallium_scan IS normal) THEN health IS sick_1;
        m10_sick1 = float(thallium['normal'])

        # RULE 47: IF (thallium_scan IS medium) THEN health IS sick_2;
        m13_sick2 = float(thallium['medium'])

        # RULE 48: IF (thallium_scan IS high) THEN health IS sick_3;
        m10_sick3 = float(thallium['high'])

        # RULE 49: IF (thallium_scan IS high) THEN health IS sick_4;
        m9_sick4 = float(thallium['high'])

        # RULE 50: IF (age IS young) THEN health IS healthy;
        m8_healthy = float(age['young'])

        # RULE 51: IF (age IS mild) THEN health IS sick_1;
        m11_sick1 = float(age['mild'])

        # RULE 52: IF (age IS old) THEN health IS sick_2;
        m14_sick2 = float(age['old'])

        # RULE 53: IF (age IS old) THEN health IS sick_3;
        m11_sick3 = float(age['old'])

        # RULE 54: IF (age IS very_old) THEN health IS sick_4;
        m10_sick4 = float(age['very_old'])

        sick_1 = [m1_sick1, m2_sick1, m3_sick1, m4_sick1, m5_sick1,
                  m6_sick1, m7_sick1, m8_sick1, m9_sick1, m10_sick1, m11_sick1]

        sick_2 = [m1_sick2, m2_sick2, m3_sick2, m4_sick2, m5_sick2,
                  m6_sick2, m7_sick2, m8_sick2, m9_sick2, m10_sick2, m11_sick2, m12_sick2, m13_sick2, m14_sick2]

        sick_3 = [m1_sick3, m2_sick3, m3_sick3, m4_sick3, m5_sick3,
                  m6_sick3, m7_sick3, m8_sick3, m9_sick3, m10_sick3, m11_sick3]

        sick_4 = [m1_sick4, m2_sick4, m3_sick4, m4_sick4, m5_sick4, m6_sick4, m7_sick4, m8_sick4, m9_sick4, m10_sick4]

        healthy = [m1_healthy, m2_healthy, m3_healthy, m4_healthy, m5_healthy, m6_healthy, m7_healthy, m8_healthy]

        inference_res = {
            'sick_1': max(sick_1),
            'sick_2': max(sick_2),
            'sick_3': max(sick_3),
            'sick_4': max(sick_4),
            'healthy': max(healthy)
        }

        return inference_res
