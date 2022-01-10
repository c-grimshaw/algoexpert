def runLengthEncoding(string):
    encoded = []
    consecutive = i = 0

    while i < len(string):
        char = string[i]
        while i + consecutive < len(string) and string[i] == string[i+consecutive]:
            if consecutive == 9:
                encoded.append(f'{consecutive}{char}')
                i += consecutive
                consecutive = 0
            else:
                consecutive += 1
        encoded.append(f'{consecutive}{char}')
        i += consecutive
        consecutive = 0 
            
    return ''.join(encoded)

runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")