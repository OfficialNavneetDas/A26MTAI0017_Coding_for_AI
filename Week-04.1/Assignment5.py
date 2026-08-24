# a list of lists, where each inner list is a batch of sensor readings.
telemetry_stream=[
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 28.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"]
]


for batch in range(len(telemetry_stream)):
    delta=None
    print(f"--- Auditing Batch {batch}: {telemetry_stream[batch]} ---")

    for reading in telemetry_stream[batch]:  
        if reading == "STOP":
            print(f"Emergency Shutdown at Batch {batch}")
            break
        
        if isinstance(reading,(int,float)):
            if reading > 35.0:
                print(f"Anomaly Detected at Batch: {batch+1}")
            if bool(delta) and reading-delta > 5.0:
                print(f"Spike detected at batch {batch}: {delta} -> {reading} (delta {reading-delta:.2f})")
                
            delta = reading
            continue
        
        if reading == "ERR":
            print(f"Noice ignored at Batch {batch} (ERR).")
            delta = None
        
    # 1. if the inner break runs then the else will not run causing the break to run and end the loop
    # 2. if the inner conditional dosen't run it will cause the else to run heance the continue will be encountered causing the break to be skipped
    else:
        continue
    break

else:
    print("Audit Complete: NO system--wide failures")
