def main():
    population = float(input('Input number of population (Million): '))
    infile = open("UN.txt", 'r')
    data = [line.rstrip().split(',') for line in infile]
    infile.close()
    
    for i in range(len(data)):
        data[i][2] = float(data[i][2])
    
    data_population = [item for item in data if item[2] >= population]
    
    for item in data_population:
        print(f'{item[0]}, {item[1]}: {item[2]}')

main()

