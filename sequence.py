# Functie die letters van de sequentie telt
def count_seq(filename):
    seq = ""
    try:    # Probeer het bestand te openen, sla de eerste lijn over en voeg elke lijn toe aan de variabele seq.
        with open(filename) as f:
            header = f.readline()[1:-1]
            # next(f)
            for line in f:
                seq += line
    except FileNotFoundError:   # Bij file not found: geef error en stop met de functie.
        print("Error: File not found.")
        return
    a_count = seq.count("A")    # Tel alle letters en sla apart op in variabelen
    g_count = seq.count("G")
    c_count = seq.count("C")
    t_count = seq.count("T")

    total = len(seq)

    print("Analyzing sequence: " + header)    # Print alle informatie
    print("Amount A:\t" + str(a_count))
    print("Amount G:\t" + str(g_count))
    print("Amount C:\t" + str(c_count))
    print("Amount T:\t" + str(t_count))
    print("Total:\t\t" + str(total))
    print("GC%\t\t\t" + str((g_count+c_count)/total*100)+"%\n")     # Bereken en print GC%
    return


# Call de functie met twee bestanden
count_seq("sapiens genomic.fasta")
count_seq("sapiens mrna.fasta")
count_seq("elegans genomic.fasta")
count_seq("elegans mrna.fasta")

