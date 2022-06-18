import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)
cursor= conn.cursor()
# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `Air_Control`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
      CREATE DATABASE `Air_Control`;
      USE `Air_Control`;

      CREATE TABLE `chaves`(
      `chave` varchar(10),
      PRIMARY KEY (`chave`));

      CREATE TABLE `cliente`(
      `id` int(10) not null auto_increment,
      `nome`  varchar(50),
      `email` varchar(20),
      `telefone` varchar(13),
      `chave` varchar(10) not null unique,
      primary key(`id`),
      foreign key(chave)references chaves(chave));'''

cursor.execute(criar_tabelas)

# inserindo usuarios
cursor.executemany(
      'INSERT INTO Air_Control.chaves VALUES (%s)',
      [
        ('chave_01'),
        ('chave_02'),
        ('chave_03'),
        ('chave_04'),
        ('chave_05'),
        ('chave_06'),
        ('chave_07'),
        ('chave_08'),
        ('chave_09'),
      ])
cursor.executemany(
      'INSERT INTO Air_Control.cliente (nome, email, telefone, chave) VALUES (%s,%s,%s,%s)',
      [
        ('Matheus', "mateu@gmail.com", "996452673", "chave_01"),
        ('Vinicius', "viny@gmail.com", "987456499", "chave_02"),
        ('Augusto', "algusto@gmail.com", "996356475", "chave_03"),
      ])

cursor.execute('select * from Air_Control.cliente')
print(' -------------  Usuários:  -------------')
for cliente in cursor.fetchall():
    print(cliente[1])



cursor.execute('select * from Air_Control.chaves')
print(' -------------  chave:  -------------')
for chave in cursor.fetchall():
    print(chave[0])

# commitando senão nada tem efeito
conn.commit()
cursor.close()