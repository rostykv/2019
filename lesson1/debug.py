def aristoteles(x, known_primes):
    counter = []
    d = known_primes[-1]
    for n in known_primes:
        counter.append([n, n - d % n])

    while True:
        d += 1
        if d>x: return
        prime = True
        for [a,b] in counter:
            b -= 1
            if b == 0:
                b = a
                prime = False
        if prime:
            yield d
            counter.append([d,d])
