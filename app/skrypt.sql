CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS sensor CASCADE;
DROP TABLE IF EXISTS forestry;
DROP TABLE IF EXISTS forest_action;
DROP TABLE IF EXISTS emergency_event;
DROP TABLE IF EXISTS sensor_readings_log;
DROP TABLE IF EXISTS sensor_emergency_event;
DROP TABLE IF EXISTS token;
SELECT *
FROM pg_available_extensions;
CREATE TABLE forestry(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	location POLYGON NOT NULL,
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY(id)
);
CREATE TABLE sensor(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	forestry_id UUID,
	location POINT NOT NULL,
	type VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_forestry FOREIGN KEY(forestry_id) REFERENCES forestry(id)
);
CREATE TABLE sensor_reading(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	sensor_id UUID NOT NULL,
	reading REAL NOT NULL,
	readTime DATERANGE NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_sensor FOREIGN KEY(sensor_id) REFERENCES sensor(id)
);
CREATE TABLE forest_action(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	forestry_id UUID NOT NULL,
	location POLYGON NOT NULL,
	type VARCHAR(100) NOT NULL,
	subtype VARCHAR(100) NOT NULL,
	time_period DATERANGE NOT NULL,
	forestry_id UUID NOT NULL,
	PRIMARY KEY(id) CONSTRAINT fk_forestry FOREIGN KEY(forestry_id) REFERENCES forestry(id)
);
CREATE TABLE sensor_readings_log(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	sensor_id UUID NOT NULL,
	time_frame TSRANGE NOT NULL,
	seconds_between_readings INTEGER NOT NULL,
	readings REAL [] NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_sensor FOREIGN KEY(sensor_id) REFERENCES sensor(id)
);
CREATE TABLE sensor_emergency_event(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	sensor_id UUID NOT NULL,
	time_of_reading TIMESTAMP NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_sensor FOREIGN KEY(sensor_id) REFERENCES sensor(id)
);
CREATE TABLE token(
	id UUID NOT NULL DEFAULT uuid_generate_v1mc(),
	value VARCHAR(100) not NULL DEFAULT uuid_generate_v1mc(),
	PRIMARY KEY(id)
);
INSERT INTO sensor(location, type, model)
VALUES ('(3.14, 6.28)', 'Smoke detector', 'SM-2000');
INSERT INTO forestry(location, name)
VALUES (
		'((3.14, 6.28),(4.14,6.27),(12.32,25.12))',
		'Test Forest'
	);
INSERT INTO forest_action(location, type, subtype, time_period)
VALUES (
		'((3.14, 6.28),(4.14,6.27),(12.32,25.12))',
		'Test type',
		'Test subtype',
		'[2021-10-20,2021-10-25]'
	);
INSERT INTO token(value)
VALUES(DEFAULT);
SELECT *
FROM sensor
LIMIT 1;
SELECT *
FROM token