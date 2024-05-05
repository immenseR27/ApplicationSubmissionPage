import utils

def get_vacancies():
    conn = utils.connect_to_db()
    sql = "SELECT position_id, position FROM positions WHERE status=1"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def check_existance(phone):
    conn = utils.connect_to_db()
    sql = "SELECT candidate_id FROM candidates WHERE phone = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (phone,))
    result = cursor.fetchall()
    return result


def check_interview(candidate):
    conn = utils.connect_to_db()
    sql = "SELECT * FROM interviews WHERE candidate_id = %s AND position_id = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (candidate.id, candidate.position_id,))
    result = cursor.fetchall()
    return result