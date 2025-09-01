import os
import time
import random 
import json

with open("luxconf.json", "r") as f:
    data = json.loads(f.read())
    world_size = int(data["world_len"])
    seed = int(data["seed"])
    if "max_objects" in data:
        max_objects = int(data["max_objects"])
    else:
        max_objects = None
    if "map_save" in data:
        map_save = bool(data["map_save"])
    else:
        map_save = False
    


class material:
    def __init__(self,material_name:str, material_numeric_value:int, material_repr:str):
        self.material_name = material_name
        self.material_numeric_value = material_numeric_value
        self.material_repr = material_repr
        self.normal_name = self.material_name
        if len(self.material_name) > 4:
            while len(self.material_name) > 4:
                self.material_name = self.material_name.replace(self.material_name[-1], '')
    
    def __str__(self):
        return f"{self.material_repr} : {self.material_name} : {self.material_numeric_value}"
    
    def __repr__(self):
        return self.__str__()
    
    def __name__(self):
        return self.normal_name


class generator:
    def __init__(self, *args, materials:list, world:list, world_size:int=world_size, seed:int=seed, numeric_world:list=[], max_objects:int=max_objects):
        self.valid_materials = materials
        self.world = world
        self.numeric_world = numeric_world
        self.world_size = world_size
        self.seed = seed
        self.max_objects = max_objects

    def __str__(self):
        return str(self.generate())
    
    
    def __repr__(self):
        return self.__str__()
    
    def __return_numeric__(self):
        return str(self.numeric_world)
    
    def __getitem__(self, key):
        return self.world[key]

    def generate(self):
        random.seed(self.seed)
        water = False
        for i in range(self.world_size):
            if self.world_size < len(self.valid_materials):
                raise ValueError("Too much objects in world")
            if len(self.valid_materials) < 2:
                raise ValueError("Not enough objects")
            if self.max_objects and len(self.valid_materials) > self.max_objects:
                raise ValueError("Amount of objects exceeds max_object count")
            random_material = random.choices(self.valid_materials)
            if water != False:
                random_repr = "#" # whatever symbol for water if you have one
            else:
                random_repr = str(random_material)[1]
            if random_repr == "^": #whatever symbol for a cave if you have one
                choice = random.randint(1, 5)
                if choice == 5:
                    continue
                else:
                    random_material = random.choices(self.valid_materials)
                    random_repr = str(random_material)[1]
            if random_repr == "#": # whatever symbol for water
                if water == True:
                    water = False
                else:
                    water = True
            self.world.append(random_repr)
            self.numeric_world.append(str(random_material)[12])
        if map_save:
            f = open("map.map", "w")
            f.write(str(self.world).replace("[", '').replace(']', '').replace(',', '').replace("'", ''))
            f.close()
        return self.world
    

