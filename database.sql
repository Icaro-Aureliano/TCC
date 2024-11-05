CREATE DATABASE `Air_Control`;
USE `Air_Control`;

CREATE TABLE `chaves`(
`chave` varchar(10),
PRIMARY KEY (`chave`));

CREATE TABLE `cliente`(
`id` int(10) not null auto_increment,
`nome`  varchar(50),
`email` varchar(100),
`telefone` varchar(25),
`chave` varchar(10) not null unique,
primary key(`id`),
foreign key(chave)references chaves(chave));

INSERT INTO `chaves` (`chave`) VALUES 
('ABC1234567'),
('XYZ9876543'),
('LMN4567890');

INSERT INTO `cliente` (`nome`, `email`, `telefone`, `chave`) VALUES 
('João Silva', 'joao.silva@email.com', '(11) 98765-4321', 'ABC1234567'),
('Maria Oliveira', 'maria.oliveira@email.com', '(21) 99876-5432', 'XYZ9876543'),
('Carlos Souza', 'carlos.souza@email.com', '(31) 91234-5678', 'LMN4567890');
