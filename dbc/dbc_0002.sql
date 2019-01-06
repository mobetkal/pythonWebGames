----------------------------------------------------
-- TABLE STATISTICS                               --
----------------------------------------------------
---/
DROP TABLE IF EXISTS STATISTICS;
---/
CREATE TABLE STATISTICS (
  id           BIGSERIAL        NOT NULL,
  login        VARCHAR(50)      NOT NULL,
  game_name    VARCHAR(100)     NOT NULL,
  points       INTEGER          NOT NULL,
  created_at   TIMESTAMP        NOT NULL,
  PRIMARY KEY (id)
);
---/
ALTER TABLE STATISTICS
  ADD CONSTRAINT UQ_STATISTICS_login UNIQUE (login);
---/
