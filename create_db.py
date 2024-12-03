import sqlite3


def create_db(filepath):
    con = sqlite3.connect(filepath)

    cur = con.cursor()

    cur.executescript("""
    --
    -- File generated with SQLiteStudio v3.4.4 on Вт дек. 3 11:57:39 2024
    --
    -- Text encoding used: UTF-8
    --
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;

    -- Table: Nomenclature
    CREATE TABLE IF NOT EXISTS Nomenclature (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, unit VARCHAR);
    INSERT INTO Nomenclature (id, name, unit) VALUES (1, 'Яблоко', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (2, 'Молоко 1л', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (3, 'Компьютер', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (4, 'УШМ угловая', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (5, 'Тест', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (6, 'Стол из цельного дуба', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (7, 'Кресло на колесиках', 'шт');
    INSERT INTO Nomenclature (id, name, unit) VALUES (8, 'Карандаши. Набор 10 шт', 'шт');

    -- Table: Request_approvals_stages
    CREATE TABLE IF NOT EXISTS Request_approvals_stages (id INTEGER PRIMARY KEY AUTOINCREMENT, approval_status VARCHAR, approved_at DATE, comment VARCHAR, stage_order INTEGER, request_id INTEGER, acceptor_id INTEGER, FOREIGN KEY (request_id) REFERENCES Requests (id), FOREIGN KEY (acceptor_id) REFERENCES Users (id));
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (18, 'Не согласовано', NULL, NULL, 0, 22, 4);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (19, 'Не согласовано', NULL, NULL, 1, 22, 1);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (20, 'Не согласовано', NULL, NULL, 2, 22, 3);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (21, 'Согласовано', '2024-11-18 17:49:26.032121', '', 1, 13, 1);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (22, 'Не согласовано', NULL, NULL, 1, 13, 3);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (23, 'Не согласовано', NULL, NULL, 1, 13, 4);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (24, 'Согласовано', NULL, '', 0, 21, 1);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (25, 'Не согласовано', NULL, NULL, 1, 21, 3);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (26, 'Не согласовано', NULL, NULL, 2, 21, 4);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (33, 'Согласовано', '2024-11-28 18:39:32.514890', '', 0, 10, 1);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (34, 'Не согласовано', NULL, NULL, 0, 10, 3);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (35, 'Не согласовано', NULL, NULL, 0, 10, 4);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (36, 'Согласовано', '2024-11-28 18:39:34.315294', '', 0, 8, 1);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (37, 'Не согласовано', NULL, NULL, 0, 8, 3);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (38, 'Не согласовано', NULL, NULL, 0, 8, 4);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (39, 'Не согласовано', NULL, NULL, 0, 8, 5);
    INSERT INTO Request_approvals_stages (id, approval_status, approved_at, comment, stage_order, request_id, acceptor_id) VALUES (44, 'Не согласовано', NULL, NULL, 1, 23, 1);

    -- Table: Request_category
    CREATE TABLE IF NOT EXISTS Request_category (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR UNIQUE);
    INSERT INTO Request_category (id, name) VALUES (1, 'Тест категория');
    INSERT INTO Request_category (id, name) VALUES (2, 'Товары');
    INSERT INTO Request_category (id, name) VALUES (3, 'Продукты');
    INSERT INTO Request_category (id, name) VALUES (4, 'Другое');
    INSERT INTO Request_category (id, name) VALUES (5, 'Работа');
    INSERT INTO Request_category (id, name) VALUES (6, 'Офис');

    -- Table: Request_items
    CREATE TABLE IF NOT EXISTS Request_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount DECIMAL,
        request_id INTEGER,
        item_id INTEGER,
        FOREIGN KEY (request_id) REFERENCES Requests(id),
        FOREIGN KEY (item_id) REFERENCES Nomenclature(id)
    );
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (1, 1, 1, 5);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (2, 1, 2, 1);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (3, 1, 7, 4);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (4, 1, 8, 4);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (6, 4, 10, 4);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (11, 7, 14, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (13, 7, 16, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (15, 7, 17, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (17, 7, 5, 4);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (22, 9, 12, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (26, 1, 15, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (27, 1234567, 13, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (28, 1, 18, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (29, 5, 19, 5);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (30, 1, 20, 5);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (34, 7, 11, 3);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (41, 10, 21, 6);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (42, 10, 21, 7);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (43, 10, 21, 5);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (44, 10, 23, 8);
    INSERT INTO Request_items (id, amount, request_id, item_id) VALUES (45, 10, 27, 8);

    -- Table: Requests
    CREATE TABLE IF NOT EXISTS Requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR,
        created_at DATE,
        status VARCHAR,
        category_id INTEGER,
        initiator_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Request_category(id),
        FOREIGN KEY (initiator_id) REFERENCES Users(id)
    );
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (1, 'test', '2024-11-06 12:17:10.674368', 'Согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (2, 'fgd', '2024-11-08 15:45:22.845127', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (5, 'sb', '2024-11-10 17:06:00.273812', 'Выполнено', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (7, ';l', '2024-11-10 17:11:35.081867', 'Отклонено', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (8, ';l', '2024-10-10 17:11:39.282473', 'Отклонено', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (10, 'тест создания', '2024-10-10 20:35:57.999001', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (11, 'Тест обновления значений', '2024-09-14 13:27:02.112965', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (12, 'Тест обновления значений', '2024-09-14 13:29:44.629092', 'Отклонено', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (13, 'Тест обновления значений', '2024-09-14 13:30:56.444580', 'Выполнено', 2, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (14, 'тест refresh', '2024-09-14 13:38:50.076278', 'Согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (15, 'NEWТест обновления значений ', '2024-09-14 13:39:36.174217', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (16, 'NEWТест обновления значений ', '2024-09-14 13:40:11.152389', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (17, 'NEWWТест обновления значений ', '2024-08-14 13:40:45.123826', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (18, 'ntcn', '2024-08-15 16:03:10.938435', 'Согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (19, 'тест от теста', '2024-07-15 18:42:19.615604', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (20, 'test', '2024-07-15 18:49:11.115297', 'Отклонено', 1, 3);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (21, 'Необходима мебель в офис', '2024-07-16 16:42:07.497181', 'Выполнено', 6, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (23, 'Требуются карандаши в офис', '2024-11-28 18:34:09.669975', 'Не согласовано', 2, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (26, 'j', '2024-11-28 18:49:13.746897', 'Не согласовано', 1, 1);
    INSERT INTO Requests (id, description, created_at, status, category_id, initiator_id) VALUES (27, 'j', '2024-11-28 18:51:08.703751', 'Не согласовано', 1, 1);

    -- Table: Users
    CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR, second_name VARCHAR, third_name VARCHAR, position VARCHAR, login VARCHAR UNIQUE NOT NULL, password VARCHAR NOT NULL, purchaser BOOLEAN NOT NULL);
    INSERT INTO Users (id, first_name, second_name, third_name, position, login, password, purchaser) VALUES (1, 'Админ', 'Админов', 'Админович', 'Администратор', 'admin', 'admin', 1);
    INSERT INTO Users (id, first_name, second_name, third_name, position, login, password, purchaser) VALUES (3, 'Наталья', 'Блэк', 'Ивановна', 'Кассир', 'test', 'test', 0);
    INSERT INTO Users (id, first_name, second_name, third_name, position, login, password, purchaser) VALUES (4, 'Олэг', 'Богомолов', 'Александрович', 'Менеджер', 'Obog', '1234', 0);
    INSERT INTO Users (id, first_name, second_name, third_name, position, login, password, purchaser) VALUES (5, 'Алексей', 'Дроздов', 'Олегович', 'Ген дир', 'АДроздов', 'Lhjpljd123', 1);

    COMMIT TRANSACTION;
    PRAGMA foreign_keys = on;
    """)

    con.commit()
    con.close()
