# Daniel Bos
# opdracht: Pizza calculator

SmallCount = int(input('Hoeveel Small pizzas wil u?'))
SmallPrice = int(9)
MediumCount = int(input('Hoeveel Medium pizzas wil u?'))
MediumPrice = int(11)
LargeCount = int(input('Hoeveel Large pizzas wil u?'))
LargePrice = int(13)

TotalPrice = int((SmallCount*SmallPrice)+(MediumCount*MediumPrice)+(LargeCount+LargePrice))

print('U heeft',SmallCount,'Small,',MediumCount,'Medium en',LargeCount,'Large pizzas besteld. Dit kost in totaal',TotalPrice,'euro')