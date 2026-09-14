"""
Program : parse_payload.py
Purpose : Parses sensor payload packets while enforcing strict positional-only and keyword-only argument passing.
Author  : Navneet Das
Date    : 14-09-2026
Course  : Coding for AI
"""

def parse_payload(raw_packet: list, delimiter: str, /, *, correction_offset: int = 0) -> tuple:
    status_tokens = raw_packet[2].split(delimiter)
    corrected_sensors = [
        value if "ERROR" in status_tokens else value + correction_offset
        for value in raw_packet[1][:]
    ]
    return raw_packet[0], corrected_sensors


#=====================================main code=====================================================
try:
    print("\t\t\tPayload Parser & Argument Testing")
    print("-" * 70)

    # ------------------------------------------------------------------
    # Test packets
    # ------------------------------------------------------------------
    packet_1 = [501, [12.5, 13.0, 11.8], "NOMINAL|CALIBRATED"]
    packet_2 = [502, [9.0, 8.5], "ERROR|SENSOR_FAULT"]
    packet_3 = [503, [1.0, 2.0], "NOMINAL"]
    packet_4 = [504, [], "NOMINAL"]
    packet_5 = [505, [10.0, 20.0, 30.0], "NOMINAL|CALIBRATED|LOW_POWER"]

    print(f"\n|-{'-'*50}-|")
    print("\n--- Test 1: Normal correction applied ---")
    result_1 = parse_payload(packet_1, "|", correction_offset=2)
    print(f"Test 1 -> ID: {result_1[0]} | Sensors: {result_1[1]}")
    assert packet_1[1] == [12.5, 13.0, 11.8], "Original packet_1 sensors were mutated!"
    assert result_1[1] is not packet_1[1], "Returned list must be a different object!"
    assert id(result_1[1]) != id(packet_1[1]), "Returned list must have a different id!"
    print("Test 1 side-effect assertions passed.")

    print("\n--- Test 2: ERROR status present -> no correction applied ---")
    result_2 = parse_payload(packet_2, "|", correction_offset=5)
    print(f"Test 2 -> ID: {result_2[0]} | Sensors: {result_2[1]}")
    assert packet_2[1] == [9.0, 8.5], "Original packet_2 sensors were mutated!"
    assert result_2[1] is not packet_2[1], "Returned list must be a different object!"
    assert result_2[1] == packet_2[1], "Values should be unchanged when ERROR is present!"
    print("Test 2 side-effect assertions passed.")

    print("\n--- Test 3: Default correction_offset (omitted entirely) ---")
    result_3 = parse_payload(packet_3, "|")
    print(f"Test 3 (default offset) -> ID: {result_3[0]} | Sensors: {result_3[1]}")
    assert result_3[1] == [1.0, 2.0], "Default offset of 0 should leave values unchanged!"

    print("\n--- Edge case: correction_offset=0 explicit vs omitted ---")
    result_3b = parse_payload(packet_3, "|", correction_offset=0)
    print(f"Edge case (offset=0 explicit) -> ID: {result_3b[0]} | Sensors: {result_3b[1]}")
    assert result_3b[1] == result_3[1], "Explicit offset=0 must behave like the default!"
    print("Edge case passed: offset=0 explicit matches offset omitted.")

    print("\n--- Edge case: Empty sensor list ---")
    result_4 = parse_payload(packet_4, "|", correction_offset=3)
    print(f"Edge case (empty sensor list) -> ID: {result_4[0]} | Sensors: {result_4[1]}")
    assert result_4[1] == [], "Empty sensor list should return an empty list!"
    print("Edge case passed: empty sensor list handled without error.")

    print("\n--- Edge case: More than two status codes ---")
    result_5 = parse_payload(packet_5, "|", correction_offset=1)
    print(f"Edge case (3+ status codes) -> ID: {result_5[0]} | Sensors: {result_5[1]}")
    assert result_5[1] == [11.0, 21.0, 31.0], "Multi-token status parsing failed!"
    print("Edge case passed: multi-token status flag parsed correctly.")
    
    print(f"\n|-{'-'*50}-|")

    print("\n--- Test 4: Illegal call - positional-only args passed as keywords ---")
    try:
        parse_payload(raw_packet=packet_1, delimiter="|")
        raise AssertionError("Test 4 failed: no TypeError was raised!")
    except TypeError as e:
        print(f"Test 4 passed. TypeError raised as expected: {e}")

    print("\n--- Test 5: Illegal call - keyword-only arg passed positionally ---")
    try:
        parse_payload(packet_1, "|", 2)
        raise AssertionError("Test 5 failed: no TypeError was raised!")
    except TypeError as e:
        print(f"Test 5 passed. TypeError raised as expected: {e}")

    print(f"\n|-{'-'*50}-|")

except AssertionError as ae:
    print(f"Assertion Error: {ae}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    input("\n\n\n\n\nPress Enter to Exit....")
