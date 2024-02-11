import pandas as pd

from itertools import permutations

max_length = 45
desired_techniques = ['True Method', 'Yin Jin Jing', 'Art of Harmony', 'Lotus in Heart', 'Breathing Skill', 'Diamond Body', 'Wu Dang Harmony', 'Mechanic', 'Poison Proof Spell']


def checksubstring(a, b):
    if not a or not b:
        return b or a
    if b in a:
        return a
    for i in range(1, len(b)):
        if a[len(a) - i:] == b[:i]:
            return a + b[i:]
    return a + b


def shortest_substring(a, b):
    x = checksubstring(a, b)
    y = checksubstring(b, a)
    return x if len(x) < len(y) else y if len(x) > len(y) else (x, y)


def shortest_sequence_in_order(incomplete_sequence):
    sequence = incomplete_sequence[0]
    sequences_to_add = incomplete_sequence[1]
    while sequences_to_add:
        sequence = shortest_substring(sequence, sequences_to_add.pop(0))
        if not isinstance(sequence, str):
            return (sequence[0], sequences_to_add.copy()), (sequence[1], sequences_to_add.copy())
    return sequence


if __name__ == '__main__':
    df = pd.read_csv('data/inner.csv', index_col=0, names=['Sequence'])
    required_sequences = [x for x in map(lambda x: df.at[x, 'Sequence'], desired_techniques)]
    all_sequence_orders = permutations(required_sequences)
    incomplete_sequences = []
    found_sequences = []
    for sequence_order in all_sequence_orders:
        incomplete_sequences.append((sequence_order[0], list(sequence_order[1:])))
        while incomplete_sequences:
            result = shortest_sequence_in_order(incomplete_sequences.pop())
            if not isinstance(result, str):
                incomplete_sequences.append(result[0])
                incomplete_sequences.append(result[1])
            elif len(result) < max_length:
                if result not in found_sequences:
                    found_sequences.append(result)
    if found_sequences:
        found_sequences = sorted(found_sequences, key=lambda x: len(x))
        shortest_len = len(found_sequences[0])
        index = 0
        print(f'shortest sequences(length of {shortest_len}) found:')
        while len(found_sequences[index]) == shortest_len:
            print(found_sequences[index])
            index += 1
    else:
        print('No sequences found')
