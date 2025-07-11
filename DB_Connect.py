import mysql.connector

def get_tone_template(persona, mood):
    # Replace these with your actual RDS credentials and details
    conn = mysql.connector.connect(
        host="localhost ",
        user=" root",
        password="Password@123",
        database="template_for_tones"
    )
    cursor = conn.cursor()
    query = "SELECT template FROM tone_templates WHERE persona = %s AND mood = %s"
    cursor.execute(query, (persona, mood))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return result[0]
    else:
        return "No template found."

# Example usage:
template = get_tone_template('elon', 'witty')
print("Fetched Template:", template)


##root@localhost:3306
##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 - API KEY 