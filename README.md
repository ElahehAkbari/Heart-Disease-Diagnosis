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

# Implementation Steps
## [Fuzzification](/fuzzification.py)
Fuzzification is the process of decomposing a system input into fuzzy sets with some degree of membership. In this step, all inputs, including the crisp ones, were fuzzified based on their provided membership functions.  
## [Inference](/inference.py)


## [Defuzzification](/defuzzification.py)
Defuzzification is the process that maps a fuzzy set to a crisp set. There are multiple defuzzification methodos that are used in fuzzy systems, one of the most widely used on of which is Center of Gravity(CoG). This method is calculated by th

![cog-equation-discrete-mf](https://user-images.githubusercontent.com/79719208/196052646-0a6969cf-3835-4231-8b49-924d02582d35.jpg)

# How to run
First, install the requirements and then run using the following commands.

```
pip install -r requirements.txt
python3 app.py
```
