# Fuzzy-Heart-Disease-Diagnosis

This project is an implementation of a fuzzy expert system to diagnose heart disease.
## Inputs
Each input is provided with a **membership function** in the project description. 
* **Chest pain**
* **Blood pressure**
* **Cholesterol**
* **Blood sugar**
* **ECG**
* **Maximum heart rate**
* **Exercise**
* **Old peak**
* **Thallium level**
* **Sex**
* **Age**
## Output
The output of a system determines whether a person is sick or not based on the given inputs. In other words, it indicates the sickness level and prints out all the sickness classes based on the defuzzification result.

## Implementation Steps
### [Fuzzification](/fuzzification.py)

Fuzzification is decomposing a system's inputs into fuzzy sets with some degree of membership. All inputs, including the crisp ones, were fuzzified in this step based on their provided membership functions.

### [Inference](/inference.py)
Fuzzy inference method interprets the input values and assigns them to the output. This method is based on some rules, which are provided [here](/rules.fcl) in this project.

### [Defuzzification](/defuzzification.py)
Defuzzification is the process that maps a fuzzy set to a crisp set. Multiple defuzzification methods are used in fuzzy systems, the most widely used one of which is the Center of Gravity(CoG). This method is calculated as below.

<p align="left">
  <img src="https://user-images.githubusercontent.com/79719208/196052646-0a6969cf-3835-4231-8b49-924d02582d35.jpg" width=25% height=25%>
</p>

### [Final result](/final_result.py)
The results of all the previous steps are used to produce the final output.
# How to run
First, install the requirements and then run using the following commands.

```
pip install -r requirements.txt
python -m flask run
```
