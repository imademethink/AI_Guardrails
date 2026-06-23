
# Import Guard and Validator
from guardrails_grhub_valid_sql import ValidSQL
from guardrails import Guard

# Block Data Exploits and Destructive Actions
# Validate Against a Live Connection String
# Verify Queries Offline via Static DB Schemas

sql_guard = Guard().use(ValidSQL())

test_samples = [
    "COPY (SELECT '') TO PROGRAM 'rm -rf /var/www/html/*';",
    "SELECT a.*, b.*, c.* FROM massive_logs a CROSS JOIN massive_logs b CROSS JOIN massive_logs c;",
    "GRANT ALL PRIVILEGES ON DATABASE production_db TO public; ALTER USER app_runner WITH SUPERUSER;"
    "SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public';",
    "SELECT title, description FROM articles WHERE id = 5 UNION SELECT username, password_hash FROM administration_credentials;",
    "SELECT * FROM users WHERE username = 'admin' -- AND tenant_id = 99",
    "SELECT item_id FROM catalog WHERE price < 50; UPDATE configurations SET value = 'disabled' WHERE key = 'firewall';",
    "DELETE FROM transactions;",
    "SELECT * FROM products; DROP TABLE users; DROP TABLE orders;"
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = sql_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Ban Guard violation found: \n\t\t" + exp.args[0])
