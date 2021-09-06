croissantAmount = int(input('Hoeveel croissants gaat u halen?'))
croissantPrice = float(0.39)
stokbrodenAmount = int(input('Hoeveel stokbroden gaat u halen?'))
stokbrodenPrice = float(2.78)
kortingsbonnenAmount = int(input('Hoeveel geldige kortingsbonnen heeft u?'))
kortingbonnenPrice = float(0.50)

totaal = int(((croissantAmount*croissantPrice)+(stokbrodenAmount*stokbrodenPrice)-(kortingsbonnenAmount*kortingbonnenPrice))*100)

print('De feestlunch kost je bij de bakker', totaal, 'cent voor de',croissantAmount,'croissantjes en de',stokbrodenAmount,'stokbroden als de',kortingsbonnenAmount,'kortingsbonnen nog geldig zijn!')