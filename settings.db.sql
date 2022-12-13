BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "code" (
	"Field1"	TEXT
);
CREATE TABLE IF NOT EXISTS "stores" (
	"code"	TEXT UNIQUE,
	"name"	TEXT
);
CREATE TABLE IF NOT EXISTS "replace" (
	"partner1c"	TEXT,
	"code1c"	TEXT,
	"code"	TEXT,
	"name"	TEXT,
	"brand"	TEXT,
	"UL"	TEXT,
	"address"	TEXT,
	"comment"	TEXT,
	UNIQUE("code","code1c")
);
COMMIT;
