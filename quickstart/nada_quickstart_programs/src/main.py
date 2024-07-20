from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))

    result = a + b

    return [Output(result, "my_output", party=party3)]

def simulate_protocol():
    input_a = 5
    input_b = 3

    protocol_output = nada_main()

    for output in protocol_output:
        if output.name == "my_output":
            print(f"Output for {output.party.name}: {output.value}")

simulate_protocol()
