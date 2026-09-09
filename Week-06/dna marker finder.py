"""
Author  : Navneet Das
Date : 09-09-2026
Course: Coding for AI
Assignment: Problem Set 6
"""

def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """Return the set of target 'letters' found in a supplied phrase"""
    return set(letters).intersection(set(phrase))

def analyze_sequence(sequence_list, marker):
    print(f" Inside Function (Start) ID: {id(sequence_list)} | Data: {sequence_list}")
    # In-place modification (mutating the shared object)
    sequence_list.append(marker)
    print(f" Inside Function (End) ID: {id(sequence_list)} | Data: {sequence_list}")


#=====================================main code=====================================================
try:
    print("\t\t\tThe DNA Sequence Marker Finder")
    print("-"*70)
    
    print("\n--- Task 1: Building search4letters ---")
    print(f"Positional arguments: {search4letters('TGGACC', 'GC')}")
    print(f"Keyword arguments: {search4letters(letters='CG', phrase='TGGACC')}")
    print(f"Defaults: {search4letters('TGGACC')}")

    print("\n--- Task 1: Edge Cases ---")
    print(f"Empty phrase: {search4letters('')}")
    print(f"Mix positional/keyword: {search4letters('TGGACC', letters='GC')}")

    print(f"\n\n\n|-{"-"*50}-|")
    print("\n--- Task 2: Tracking Memory References (Core Demo) ---")
    
    dna_database = ['AATCCG', 'TGGCTA']
    print(f" Global Scope (Before) ID: {id(dna_database)} | Data: {dna_database}")
    analyze_sequence(dna_database, 'CGAT')
    print(f" Global Scope (After) ID: {id(dna_database)} | Data: {dna_database}")

    print("\n--- Task 2: The Slice Experiment ---")
    dna_database_sliced = ['AATCCG', 'TGGCTA']
    print(f" Global Scope (Before Slice) ID: {id(dna_database_sliced)} | Data: {dna_database_sliced}")
    analyze_sequence(dna_database_sliced[:], 'CGAT')
    print(f" Global Scope (After Slice) ID: {id(dna_database_sliced)} | Data: {dna_database_sliced}")
    
    print("\n--- Task 2: Slice Edge Case (Repeated Calls) ---")
    analyze_sequence(dna_database_sliced[:], 'CGAT')
    
    print(f"|-{"-"*50}-|")

except ValueError as ve:
    print(ve)
finally:
    input("\n\n\n\n\nPress Enter to Exit....")
