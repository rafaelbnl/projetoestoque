CREATE DATABASE estoque;
USE estoque;

CREATE TABLE produtos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(60) NOT NULL UNIQUE,
marca VARCHAR(60) NOT NULL,
qtd_disponivel INT NULL,
valor_unitario DECIMAL(6,2) NOT NULL);

INSERT INTO produtos (nome, marca, qtd_disponivel, valor_unitario) VALUES
('Arroz Branco 5kg', 'Tio João', 50, 28.90),
('Feijão Preto 1kg', 'Camil', 40, 8.50),
('Açúcar Refinado 1kg', 'União', 60, 4.20),
('Sal Refinado 1kg', 'Cisne', 80, 2.50),
('Óleo de Soja 900ml', 'Liza', 45, 7.80),
('Macarrão Espaguete 500g', 'Barilla', 70, 6.90),
('Molho de Tomate 340g', 'Pomarola', 55, 3.50),
('Café Torrado 500g', 'Pilão', 35, 15.90),
('Leite Integral 1L', 'Parmalat', 100, 5.20),
('Manteiga 200g', 'Itambé', 30, 12.50),
('Queijo Mussarela 500g', 'Tirolez', 25, 32.90),
('Presunto Fatiado 200g', 'Sadia', 28, 14.90),
('Pão de Forma Integral', 'Wickbold', 45, 8.90),
('Biscoito Cream Cracker', 'Adria', 65, 4.50),
('Achocolatado em Pó 400g', 'Nescau', 40, 9.80),
('Refrigerante Cola 2L', 'Coca-Cola', 90, 8.50),
('Suco de Laranja 1L', 'Del Valle', 55, 7.20),
('Água Mineral 1.5L', 'Crystal', 120, 2.80),
('Sabão em Pó 1kg', 'Omo', 35, 16.90),
('Detergente Líquido 500ml', 'Ypê', 50, 3.20),
('Papel Higiênico 12 rolos', 'Neve', 40, 18.50),
('Shampoo 400ml', 'Seda', 30, 12.90),
('Sabonete 90g', 'Dove', 60, 3.80),
('Creme Dental 90g', 'Colgate', 55, 6.50),
('Desinfetante 2L', 'Pinho Sol', 38, 11.90),
('Esponja de Lã de Aço', 'Bombril', 75, 4.20),
('Amaciante 2L', 'Comfort', 32, 14.50),
('Farinha de Trigo 1kg', 'Dona Benta', 48, 5.90),
('Extrato de Tomate 340g', 'Elefante', 42, 4.80),
('Vinagre 750ml', 'Castelo', 50, 3.50);