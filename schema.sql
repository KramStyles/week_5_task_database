CREATE TABLE songs
(
    id integer NOT NULL SERIAL,
    user_id integer NOT NULL,
    name character varying(100) NOT NULL,
    genre character varying(50) NOT NULL,
    created_at date NOT NULL,
    updated_at date,
    PRIMARY KEY (id)
);

CREATE TABLE users
(
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    created_at date NOT NULL,
    updated_at date,
    PRIMARY KEY (id)
);