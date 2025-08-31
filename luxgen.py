import os
import time
import random 
import json

with open("luxconf.json", "r") as f:
    data = json.loads(f.read())
    world_size = int(data["world_len"])
    seed = int(data["seed"])
    max_objects = int(data["max_objects"])
    


world_list = []
world_numeric = []
materials_list = []


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
    def __init__(self, *args, materials:list, world:list, world_size:int=10, seed:int=123456, numeric_world:list, max_objects:int=None):
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
        for i in range(self.world_size):
            if self.world_size < len(self.valid_materials):
                raise ValueError("Too much objects in world")
            if len(self.valid_materials) < 2:
                raise ValueError("Not enough objects")
            if self.max_objects and len(self.valid_materials) > self.max_objects:
                raise ValueError("Amount of objects exceeds max_object count")
            random_material = random.choices(self.valid_materials)
            random_repr = str(random_material)[1]
            self.world.append(random_repr)
            self.numeric_world.append(str(random_material)[12])
        return self.world







if __name__ == "__main__":
    materials_list.append(material("Moss", "1", "~"))
    materials_list.append(material("Vine", "2", "_"))
    materials_list.append(material("Water", "3", "#"))
    materials_list.append(material("Tree", "4", "T"))
    materials_list.append(material("Bolder", "5", "*"))
    materials_list.append(material("Cave", "6", "^"))

    gen1 = generator(materials=materials_list, world=world_list, world_size=world_size, seed=seed, numeric_world=world_numeric)
    gen2 = generator(materials=materials_list, world=world_list, world_size=world_size, seed=seed, numeric_world=world_numeric) # remove if not making 2d map
    map = [ # remove if not making 2d map
        gen1, 
        gen2
    ]
    print(str(map).replace("[", '').replace("]", '').replace("'", '').replace(",", '').strip()) # replace to print(str(gen1)) if not using 2d map
    #print(gen1.__return_numeric__()) if you want numeric values of each object in the 1d map
