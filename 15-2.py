def main():
    infile = open("UN.txt", 'r')
    data = [line.rstrip() for line in infile]
    infile.close()
    print(data)

main()

