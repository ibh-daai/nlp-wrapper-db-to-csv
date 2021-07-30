# This is script 1 of 2 to wrap around an NLP algorithm like CheXpert, this script reads reports from a database and
# dumps it into CSV format, which is easy to use by the existing label.py script

import psycopg2, psycopg2.extras, datetime, csv

if __name__ == "__main__":
    writer = csv.writer(open("input.csv", "w", newline=''))
    pgconn = psycopg2.connect("host='pghost' dbname='pgdb' user='pguser' password='pgpass' client_encoding='UTF8'")
    pgconn.autocommit = True
    pgsql = pgconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = """SELECT s.study_id, s.report_text
            FROM study s
            LEFT JOIN nlp_results nr ON (s.study_id=nr.study_id AND nr.algorithm_id=6)
            WHERE modality IN ('CR','DX') AND nr.results IS NULL
            ORDER BY s.study_id LIMIT 500"""
    pgsql.execute(sql)
    rows = pgsql.fetchall()
    writer.writerow(['Report Impression','study_id'])
    for row in rows:
        writer.writerow([row['report_text'],row['study_id']])
