from cats import Tiger
from dogs import Dog

dog_name = "Bobik"
dog = Dog(dog_name)
dog.say()
dog_energy = dog.get_energy()
assert dog_energy == 100, "Bad start energy for Bobik"
dog.run()
dog_energy_after_run = dog.get_energy()
assert dog_energy_after_run == 90, "Bad after run energy for Bobik"
dog.swim()
dog_energy_after_swim = dog.get_energy()
assert dog_energy_after_swim == 60, "Bad after swim energy for Bobik"
dog.fly()
dog_energy_after_fly = dog.get_energy()
assert dog_energy_after_fly == 60, "Bad after fly energy for Bobik"

tiger_name = "Barsik"
tiger = Tiger(tiger_name)
tiger.say()
tiger_energy = tiger.get_energy()
assert tiger_energy == 200, "Bad start energy for Barsik"
tiger.run()
tiger_energy_after_run = tiger.get_energy()
assert tiger_energy_after_run == 180, "Bad after run energy for Barsik"
tiger.swim()
tiger_energy_after_swim = tiger.get_energy()
assert tiger_energy_after_swim == 140, "Bad after swim energy for Barsik"
tiger.fly()
tiger_energy_after_fly = tiger.get_energy()
assert tiger_energy_after_fly == 140, "Bad after fly energy for Barsik"
