--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- drop tables
---


DROP TABLE IF EXISTS centauro_prices;
DROP TABLE IF EXISTS mercado_livre_prices;
DROP TABLE IF EXISTS bitcoin_prices;
DROP TABLE IF EXISTS ethereum_prices;

--
-- Name: centauro_prices; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE IF NOT EXISTS centauro_prices (
  id SERIAL PRIMARY KEY,
  brand VARCHAR(100),
  name VARCHAR(300),
  old_price_reais VARCHAR(20),
  new_price_reais VARCHAR(20),
  reviews_rating_number VARCHAR(10),
  page_count INT,
  _source_name VARCHAR(100),
  _source_link TEXT,
  _data_coleta TIMESTAMP
);

--
-- Name: mercado_livre_prices; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE IF NOT EXISTS mercado_livre_prices (
  id SERIAL PRIMARY KEY,
  brand VARCHAR(100),
  name VARCHAR(300),
  old_price_reais VARCHAR(20),
  new_price_reais VARCHAR(20),
  reviews_rating_number VARCHAR(10),
  page_count INT,
  _source_name VARCHAR(100),
  _source_link TEXT,
  _data_coleta TIMESTAMP
);

--
-- Name: bitcoin_prices; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE IF NOT EXISTS bitcoin_prices (
    id SERIAL PRIMARY KEY,
    amount_usd NUMERIC NOT NULL,
    amount_brl NUMERIC NOT NULL,
    base VARCHAR(10) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

--
-- Name: ethereum_prices; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE IF NOT EXISTS ethereum_prices (
    id SERIAL PRIMARY KEY,
    amount_usd NUMERIC NOT NULL,
    amount_brl NUMERIC NOT NULL,
    base VARCHAR(10) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);
