calibration_feed=[
    [201, 6.0, 9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204,2.75,"HALT",6.0]
]


batch_Suppressing=0
feed_cursor = 0
maximum=0
minimum=999
valid_batch_sum = 0
checksum=0
while(current_slice := calibration_feed[feed_cursor:feed_cursor+1]):
    batch = current_slice[0]

    #finging the length of the batch by for loop
    batch_length = 0
    for _ in batch:
        batch_length +=1

    #displaying only if the size is greater then 0
    if batch_length > 0:
        print(f"Evaluating batch {feed_cursor} (ID: {batch[0]}) .....")
    else:
        print(f"batch {feed_cursor} is EMPTY. Proceeding.")
        feed_cursor +=1
        continue

    # Manual backword Traversal
    for i in range(1,batch_length):
        target_index = i
        reading = batch[target_index] 

        #storing the maximum and the minimum readings for the digits

        # Control signal "HALT"
        if reading == "HALT":
            print("Signal Halt detected Executing emergency protocol")
            print(f"\n{"="*50}")
            print("CALIBRATION COMPLETE: EMERGENCY TERMINATION")
            valid_batch_sum = 0
            break

        # Control signal "FAULT"
        if reading == "FAULT":
            print(f"Signal FAULT detected Suppressing batch [{batch[0]}]")
            batch_Suppressing=1
            valid_batch_sum = 0
            break
        
        if reading == "IGNORE":
            print(f"Signal IGNORE encountered at batch [{batch[0]}]")

        if isinstance(reading,(int,float)):
            valid_batch_sum +=reading

        if isinstance(reading, (int, float)):  
            maximum = reading if reading > maximum else maximum
            minimum = reading if reading < minimum else minimum
            
    else:
        checksum += (valid_batch_sum*0.8)
        feed_cursor +=1
        continue

    #supressing the loop:
    if batch_Suppressing == 1:
        feed_cursor +=1
        continue
    else:
        break

print("\n")
print("="*50)
print("Total valid reading processed: ")
print(f"Global Calibration Checksum: ",checksum)
print("Maximum reading Encountered: ",maximum)
print("minimum reading Encountered: ",minimum)
        
