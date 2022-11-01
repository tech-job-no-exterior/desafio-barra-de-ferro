import json
import os
from pathlib import Path
import time

#from solution1 import max_price #dfs 
#from solution2 import max_price #dfs + dp 
#from solution3 import max_price #dfs + dp v2
from solution4 import max_price #dfs + dp v2 + divide to conquer

####################################################################
### asserts 
bar_size = 0
price_map = []
assert max_price(bar_size=bar_size, price_map=price_map) is False, "Should be False"

bar_size = 1
price_map = [2, 30]
assert max_price(bar_size=bar_size, price_map=price_map) is False, "Should be False"

bar_size = 10
price_map = [35,7,35,84,21,31,4,58,77,20]
assert max_price(bar_size, price_map) == 350, "Should be 350"

bar_size = 5
price_map = [5,2,10,50,20]
assert max_price(bar_size=bar_size, price_map=price_map) == 55, "Should be 55"

####################################################################
### simple tests
inputs = [
    (4, [1,5,15,60])
    ,(5, [5,2,10,50,20])
    ,(10, [35,7,35,84,21,31,4,58,77,20])    
]

for bar_size, price_map in inputs:
    print('Inputs: ', bar_size, price_map)
    start = time.perf_counter()
    price = max_price(bar_size, price_map)
    end = time.perf_counter()
    print("Result: ", price)
    print(f"Best price calculated in {end - start:0.10f} seconds")
    print("=========================")    
   
####################################################################
### load tests
current_path = os.path.join( os.path.dirname( __file__ ), '..' )
current_path.encode('unicode_escape')
current_path = current_path.replace('\\','/') 
jsons_path = str(Path(current_path).parents[2])
jsons_path.encode('unicode_escape')
jsons_path = jsons_path.replace('\\','/') + "/datasets/stored/"

files = [
    'single-bar-5.json',
    'single-bar-10.json',
    'single-bar-100.json',
    'single-bar-1000.json',
    'single-bar-10000.json',
    'single-bar-100000.json',
    'single-bar-1000000.json',
]

for file in files:
    file_path = jsons_path + file
    json_data = [] 
    
    with open(file=file_path) as json_file:
        json_data = json.load(json_file)
        print('Inputs: ', len(json_data))
        #print('Inputs: ', len(json_data), json_data)
        
        start = time.perf_counter()
        price = max_price(bar_size=len(json_data), price_map=json_data)
        end = time.perf_counter()
        
        print("Result: ", price)
        print(f"Best price calculated in {end - start:0.10f} seconds")
        print("=========================")