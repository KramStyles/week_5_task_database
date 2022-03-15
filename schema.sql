DROP TABLE users;
DROP TABLE songs;

CREATE TABLE users
(
    id SERIAL NOT NULL PRIMARY KEY ,
    username character varying(50) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    created_at date NOT NULL,
    updated_at date
);

CREATE TABLE songs
(
    id SERIAL NOT NULL PRIMARY KEY ,
    user_id integer NOT NULL REFERENCES users(id) ON DELETE CASCADE ,
    name character varying(100) NOT NULL,
    genre character varying(50) NOT NULL,
    created_at date NOT NULL,
    updated_at date
);
