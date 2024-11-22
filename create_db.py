import sqlite3


def create_db(filepath):
    con = sqlite3.connect(filepath)

    cur = con.cursor()

    cur.executescript("""
    CREATE TABLE Access_rights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice BOOLEAN,
        requests BOOLEAN
    );

    CREATE TABLE Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR,
        second_name VARCHAR,
        third_name VARCHAR,
        position VARCHAR,
        login VARCHAR UNIQUE,
        password VARCHAR,
        access_right_id INTEGER,
        FOREIGN KEY (access_right_id) REFERENCES Access_rights(id)
    );

    CREATE TABLE Vendor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        address VARCHAR
    );

    CREATE TABLE Vendor_managers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR,
        second_name VARCHAR,
        third_name VARCHAR,
        position VARCHAR,
        vender_id INTEGER,
        FOREIGN KEY (vender_id) REFERENCES Vendor(id)
    );

    CREATE TABLE Nomenclature_category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        parent_category_id INTEGER,
        FOREIGN KEY (parent_category_id) REFERENCES Nomenclature_category(id)
    );

    CREATE TABLE Nomenclature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        unit VARCHAR,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Nomenclature_category(id)
    );

    CREATE TABLE Vendor_nomenclature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        nomenclature_id INTEGER,
        FOREIGN KEY (nomenclature_id) REFERENCES Nomenclature(id)
    );

    CREATE TABLE Request_category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR
    );

    CREATE TABLE Requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR,
        created_at DATE,
        status VARCHAR,
        category_id INTEGER,
        initiator_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Request_category(id),
        FOREIGN KEY (initiator_id) REFERENCES Users(id)
    );

    CREATE TABLE Request_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount DECIMAL,
        request_id INTEGER,
        item_id INTEGER,
        FOREIGN KEY (request_id) REFERENCES Requests(id),
        FOREIGN KEY (item_id) REFERENCES Nomenclature(id)
    );

    CREATE TABLE Invoice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_name VARCHAR,
        description VARCHAR,
        created_at DATE,
        vender_manager_id INTEGER,
        purchaser_id INTEGER,
        FOREIGN KEY (vender_manager_id) REFERENCES Vendor_managers(id),
        FOREIGN KEY (purchaser_id) REFERENCES Users(id)
    );

    CREATE TABLE Invoice_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount DECIMAL,
        invoice_id INTEGER,
        vender_item_id INTEGER,
        request_item_id INTEGER,
        FOREIGN KEY (invoice_id) REFERENCES Invoice(id),
        FOREIGN KEY (vender_item_id) REFERENCES Vendor_nomenclature(id),
        FOREIGN KEY (request_item_id) REFERENCES Request_items(id)
    );

    CREATE TABLE Approval_templates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        description VARCHAR
    );

    CREATE TABLE Template_approval_stages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stage_order INTEGER,
        acceptor_id INTEGER,
        template_id INTEGER,
        FOREIGN KEY (acceptor_id) REFERENCES Users(id),
        FOREIGN KEY (template_id) REFERENCES Approval_templates(id)
    );

    CREATE TABLE Request_approvals_stages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        approval_status VARCHAR,
        approved_at DATE,
        comment VARCHAR,
        stage_order INTEGER,
        request_id INTEGER,
        template_stage_id INTEGER,
        acceptor_id INTEGER,
        FOREIGN KEY (request_id) REFERENCES Requests(id),
        FOREIGN KEY (template_stage_id) REFERENCES Template_approval_stages(id),
        FOREIGN KEY (acceptor_id) REFERENCES Users(id)
    );

    CREATE TABLE Invoice_approvals_stages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        approval_status VARCHAR,
        approved_at DATE,
        comment VARCHAR,
        stage_order INTEGER,
        invoice_id INTEGER,
        template_stage_id INTEGER,
        acceptor_id INTEGER,
        FOREIGN KEY (invoice_id) REFERENCES Invoice(id),
        FOREIGN KEY (template_stage_id) REFERENCES Template_approval_stages(id),
        FOREIGN KEY (acceptor_id) REFERENCES Users(id)
    );
    """)

    cur.execute("""
    INSERT INTO Invoice(invoice_name) VALUES ("Счет1"), ("Счет2"), ("Счет3");
    """)

    con.commit()
    con.close()
