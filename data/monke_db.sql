/*-- Предоставить права на таблицу cameras
GRANT ALL PRIVILEGES ON TABLE cameras TO dmitry;

-- Предоставить права на таблицу zones
GRANT ALL PRIVILEGES ON TABLE zones TO dmitry;

-- Предоставить права на все последовательности (для SERIAL и других)
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO dmitry;

-- Предоставить права на использование схемы public
GRANT ALL ON SCHEMA public TO dmitry;
-- Изменить владельца таблицы cameras
ALTER TABLE cameras OWNER TO dmitry;

-- Изменить владельца таблицы zones
ALTER TABLE zones OWNER TO dmitry;*/

--drop table cameras, zones;
select * from cameras, zones;
/*SELECT grantee, privilege_type 
FROM information_schema.role_table_grants 
WHERE table_name='cameras' AND grantee = 'dmitry';*/