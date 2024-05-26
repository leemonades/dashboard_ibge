import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def format_moeda(value):
    value = float(value)
    return locale.currency(value, grouping=True, symbol='R$')

def format_populacao(value):
    return '{:,}'.format(int(value)).replace(',', '.')
