DROP TABLE IF EXISTS entradas;
CREATE TABLE entradas (
    id INTEGER PRIMARY KEY autoincrement,
    titulo string NOT NULL,
    texto string NOT NULL,
    criado_em DATETIME default now
);