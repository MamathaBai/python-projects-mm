motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[0].title())
motorcycles[0] = 'ford'
print(motorcycles[0].title())
print(motorcycles)
motorcycles.append('Toyota')
print(motorcycles)
motorbikes = []
motorbikes.append('benz')
motorbikes.append('bmw')
print(motorbikes)
motorbikes.insert(0,'subaru')
print(motorbikes)
del motorbikes[0]
print(motorbikes)
motorbikes.pop()
print(motorbikes)