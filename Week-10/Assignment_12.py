"""
Program : Throughput Telemetry log Inspector
purpose : correctly reassemble complete line from a stream of raw bit chunks carrying incomplete data across chunks boundaries
and keyword-only argument passing.
Author : Navneet das
Date : 30-09-2026
"""
import os
from typing import Tuple

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

def process_log_stream(file_path: str, chunk_size: int,/) -> Tuple[int,float]:
    no_end=True
    valid_record_count = 0
    mean_sensor_value = 0
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"target path: {filepath} not found")
    leftover = b""
    
    with open ( file_path , "rb") as file_obj :
        for chunk in iter(lambda:file_obj.read(chunk_size),b"") :
            leftover += chunk
            *complete_lines , leftover = leftover.split( b"\n")
            for raw_line in complete_lines :
                splited_data = raw_line.split(b",")
                if len(splited_data) == 3 and is_float(splited_data[-1]):
                    valid_record_count+=1
                    mean_sensor_value += float(splited_data[-1])
                if splited_data[0] == b"END_OF_LOG\r":
                    no_end = False
                    break
        if no_end:
            print("warning! that the file may be truncated")
        mean_sensor_value = mean_sensor_value/valid_record_count
        return valid_record_count,mean_sensor_value
                    

for chunk_size in [1,3,7,16,32,64,128,1000]:
    ans = process_log_stream("D:\\M.tech\\coding for ai\\Week-10\\log.csv",20)
    print(f"chunk_size =   {chunk_size}\t-> {ans}")
