CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            phone text,
            country_id text,
            fm text,
            password text,
            employeetype text,
            pic text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
insert into country (name) values ('france');
insert into country (name) values ('espagne');
insert into country (name) values ('italie');
insert into country (name) values ('allemagne');
insert into country (name) values ('royaume-uni');
create table if not exists quotes(
        id integer primary key autoincrement,
        name text,
            author text,
            fm text
                    );
create table if not exists songs(
        id integer primary key autoincrement,
        artist_id text,
            title text
                    );
create table if not exists artists(
        id integer primary key autoincrement,
        name text,
            fm text
                    );
create table if not exists photo_posted(
        id integer primary key autoincrement,
        pic text,
            user_id text
                    );
