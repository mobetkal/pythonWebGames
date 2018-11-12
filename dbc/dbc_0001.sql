----------------------------------------------------
-- TABLE USERS                                    --
----------------------------------------------------
---/
DROP TABLE IF EXISTS USERS;
---/
CREATE TABLE USERS (
  id           BIGSERIAL             NOT NULL,
  login        VARCHAR(50)           NOT NULL,
  password     VARCHAR(100)          NOT NULL,
  first_name   VARCHAR(100)          NOT NULL,
  last_name    VARCHAR(100)          NOT NULL,
  display_name VARCHAR(50)           NOT NULL,
  created_at   TIMESTAMP             NOT NULL,
  PRIMARY KEY (id)
);
---/
ALTER TABLE USERS
  ADD CONSTRAINT UQ_USERS_login UNIQUE (login);
---/
