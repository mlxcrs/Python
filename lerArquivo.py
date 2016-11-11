import traceback
# Tente receber o nome do arquivo
try:
    fn = raw_input('Nome do arquivo: ').strip()
    for i, s in enumerate(file(fn)):
        print i + 1, s,
    # Se ocorrer um erro
except:
    # Mostre na tela
    trace = traceback.format_exc()
    # E salve num arquivo
    print 'Aconteceu um erro:\n', trace
    file('trace.log', 'a').write(trace)
    # Encerre o programa
    raise SystemExit