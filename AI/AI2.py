class Fact:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Rule:
    def __init__(self, conditions, result):
        self.conditions = conditions
        self.result = result

class ExpertSystem:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chain(self):
        # Implement forward chaining logic here
        pass

    def backward_chain(self, goal):
        # Implement backward chaining logic here
        pass

# Usage
system = ExpertSystem()
system.add_fact(Fact("Symptom1", "Value1"))
system.add_fact(Fact("Symptom2", "Value2"))
system.add_rule(Rule(["Symptom1", "Symptom2"], "Diagnosis"))
system.forward_chain()
system.backward_chain("Diagnosis")
