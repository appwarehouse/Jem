CREATE TABLE announcements (
    id SERIAL PRIMARY KEY,
    run_status VARCHAR(255) DEFAULT 'scheduled',
    scheduled_time TIMESTAMP,
    announcement_message VARCHAR(255),
    client_id INTEGER,
    is_scheduled BOOLEAN DEFAULT FALSE
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    announcement_id INTEGER REFERENCES announcements(id),
    message VARCHAR(255),
    recipient_number VARCHAR(20),
    status VARCHAR(255) DEFAULT 'created',
    status_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    error_message VARCHAR(255),
    retries INTEGER DEFAULT 0,
    sent BOOLEAN DEFAULT FALSE
);

CREATE TABLE contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    phoneNumber VARCHAR(20),
    client_id INTEGER
);

INSERT INTO contacts (name, surname, phoneNumber, client_id)
VALUES 
  ('Tawanda', 'Smith', '+277700000001', 1),
  ('Mpho', 'Johnson', '+276600000002', 2),
  ('Charlie', 'Shumba', '+277400000003', 3),
  ('Dudu', 'Jones', '+277300000004', 4),
  ('Emma', 'Brown', '+276400000005', 5),
  ('Frank', 'Dube', '+278300000006', 1),
  ('Grace', 'Miller', '+278200000007', 2),
  ('Henry', 'Wilson', '+277300000008', 3),
  ('Ivy', 'Gwati', '+277100000009', 4),
  ('Jack', 'Taylor', '+278400000010', 5),
  ('Tawanda', 'Shumba', '+277400000011', 1),
  ('Mpho', 'Jones', '+277300000012', 2),
  ('Charlie', 'Brown', '+276400000013', 3),
  ('Dudu', 'Dube', '+278300000014', 4),
  ('Emma', 'Miller', '+278200000015', 5),
  ('Frank', 'Wilson', '+277300000016', 1),
  ('Grace', 'Gwati', '+277100000017', 2),
  ('Henry', 'Taylor', '+278400000018', 3),
  ('Ivy', 'Shumba', '+277400000019', 4),
  ('Jack', 'Jones', '+277300000020', 5),
  ('Tawanda', 'Brown', '+276400000021', 1),
  ('Mpho', 'Dube', '+278300000022', 2),
  ('Charlie', 'Miller', '+278200000023', 3),
  ('Dudu', 'Wilson', '+277300000024', 4),
  ('Emma', 'Gwati', '+277100000025', 5),
  ('Frank', 'Taylor', '+278400000026', 1),
  ('Grace', 'Shumba', '+277400000027', 2),
  ('Henry', 'Jones', '+277300000028', 3),
  ('Ivy', 'Brown', '+276400000029', 4),
  ('Jack', 'Dube', '+278300000030', 5);


