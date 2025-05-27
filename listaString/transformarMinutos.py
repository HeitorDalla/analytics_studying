def transformado (hora: str) -> float:
    minutos = 0

    separado = hora.split()

    for i in separado:
        i = i.strip()

        try :
            if ('h' in i):
                h = int(i.replace('h', ''))
                minutos += (h * 60)

            elif ('m' in i):
                m = int(i.replace('m', ''))
                minutos += m

            else:
                s = int(i.replace('s', ''))
                minutos += (s / 60)
        except:
            print("Erro ao processar parte da string!")

    return minutos

hora = '23h 53m'

formatado = transformado(hora)

print("{} tem {} minutos" .format(hora, formatado))