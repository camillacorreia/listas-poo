class Usuario:
  '''Um usuário da rede social é unicamente identificado
  pelo seu número de telefone.'''
  def __init__(self, telefone, nome):
    self.telefone = telefone
    self.nome = nome

  def __eq__(self, outro):
    if isinstance(outro,Usuario) and self.telefone == outro.telefone:
        return True
    else:
        return False

  def __str__(self):
    return "Nome: " + str(self.nome) + " Telefone: " + str(self.telefone) + "\n"

class Grupo:
  '''Grupo de usuários na rede social.
  Um grupo possui um nome e um conjunto de membros.
  Além disso, ele possui exatamente um dono, que é um membro.
  Um grupo não pode estar vazio.
  '''

  def __init__(self, nome, dono):
    self.nome = nome
    self.dono = dono
    self.usuarios = [dono]

  def adiciona(self, usuario):
    '''Adiciona usuário como membro do grupo'''
    self.usuarios.append(usuario)
  
  def remove(self, usuario):
    '''Remove um usuário do grupo, se possível.
    Em alguns casos NÃO é possível remover o usuário do grupo:
    * Se o usuário é o único membro do grupo
    * Se o usuário é dono do grupo
    * Se o usuário não pertence ao grupo
    :return: `True` se o usuário foi removido ou `False` caso contrário
    '''
    if len(self.usuarios) > 1 and usuario != self.dono and usuario in self.usuarios:
        self.usuarios.remove(usuario)
        return True
    else: 
        return False

  def altera_dono(self, novo_dono):
    '''Destitui o dono atual e elege um novo dono.
    O dono deve ser membro do grupo.
    Retorna `True` se o usuário informado é o novo dono
    ou `False` caso contrário.
    '''
    if novo_dono in self.usuarios:
        self.dono = novo_dono
        return True
    else:
        return False

  def contem_membro(self, usuario):
    '''Indica se um usuário faz parte do grupo'''
    if usuario in self.usuarios:
        return True
    else:
        return False

  def membros(self):
    '''Retorna uma cópia da lista de membros'''
    return self.usuarios.copy

  def tamanho(self):
    '''Retorna quantidade de membros'''
    return len(self.usuarios)

### Testes
import unittest

class TestUsuario(unittest.TestCase):
  def test_iguais(self):
    a = Usuario('123', 'abc')
    b = Usuario('123', 'abc')
    self.assertEqual(a, b)
  
  def test_mesmo_telefone_nome_diferente(self):
    a = Usuario('123', 'abc')
    b = Usuario('123', 'def')
    self.assertEqual(a, b)
  
  def test_diferentes(self):
    a = Usuario('123', 'abc')
    b = Usuario('124', 'abc')
    self.assertNotEqual(a, b)


class TestGrupo(unittest.TestCase):
  def teste_cria_grupo(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    self.assertEqual(g.nome,'POO')
    self.assertEqual(g.dono,u)
    self.assertIn(u,g.usuarios)

  def teste_adiciona_usuario(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    g.adiciona(a)
    self.assertIn(a,g.usuarios)

  def teste_remove_usuario_sucesso(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    g.adiciona(a)
    self.assertEqual(g.remove(u),False)
    g.remove(a)
    self.assertNotIn(a,g.usuarios)
  
  def teste_remove_usuario_falha_dono_tamanho(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    g.adiciona(a)
    self.assertEqual(g.remove(u),False)
    g.remove(u)
    self.assertIn(u,g.usuarios)
  
  def teste_remove_usuario_falha_usuario(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    d = Usuario('71993009833','Pedro')
    g.adiciona(a)
    self.assertEqual(g.remove(d),False)
    g.remove(d)
    self.assertNotIn(d,g.usuarios)

  def teste_altera_dono(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    d = Usuario('71993009833','Pedro')
    g.adiciona(a)
    g.altera_dono(a)
    self.assertEqual(g.dono,a)
    self.assertEqual(g.altera_dono(d),False)

  def teste_contem_membro(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    d = Usuario('71993009833','Pedro')
    g.adiciona(a)
    self.assertEqual(g.contem_membro(a),True)
    self.assertEqual(g.contem_membro(d),False)

  def teste_membros(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    d = Usuario('71993009833','Pedro')
    g.adiciona(a)
    g.adiciona(d)
    self.assertEqual(g.membros(),g.usuarios)

  def teste_tamanho(self):
    u = Usuario('71993009831','Caio')
    g = Grupo('POO',u)
    a = Usuario('71993009830','Felipe')
    d = Usuario('71993009833','Pedro')
    g.adiciona(a)
    g.adiciona(d)
    self.assertEqual(g.tamanho(),3)


if __name__ == '__main__':
  import sys
  unittest.main(exit=False)