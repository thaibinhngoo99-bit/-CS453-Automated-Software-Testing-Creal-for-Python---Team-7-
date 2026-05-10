import datetime
from dateutil.relativedelta import relativedelta

print("Programa para calcular o prazo de exame de ultrassom...\nO mesmo deve ser feito entre 22 e 24 semanas de gestação")
print("você deverá informar com quantas semanasa de gestação a paciente se encontra, no formato aaaa/mm/dd")
semanas = int(input("Com quantas semanas de gestação a paciente se encontra hoje? "))
exameInicio = 22-semanas
exameFinal = 24 - semanas

morfologicoInicio = datetime.date.today()+ relativedelta(weeks=exameInicio)
morfologicoFinal = datetime.date.today() + relativedelta(weeks=exameFinal)
dfinal = morfologicoFinal.strftime('%d/%m/%Y')
dinicial = morfologicoInicio.strftime('%d/%m/%Y')
print("O exame deverá ser feito entre ",dinicial, " e ", dfinal)