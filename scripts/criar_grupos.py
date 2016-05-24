#!/user/bin/python
import django.contrib.auth.models.Group

names = ['Administrador', 'Autor', 'Operador de Administração',
         'Operador de Comissão', 'Operador de Matéria Legislativa',
         'Operador de Norma Juridica', 'Operador de Protocolo',
         'Operador de Sessão', 'Operador Geral']

for n in names:
    Group.objects.create(name=n)
