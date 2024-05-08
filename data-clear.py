import sqlite3

# Database file path, ensure this matches the path used in your Flask application
DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def clear_test_contacts():
    """Clear only the test contacts from the database."""
    db = connect_db()
    # Assuming all test contacts follow a specific naming pattern
    db.execute("DELETE FROM contacts WHERE name LIKE 'Test Name %'")
    # Also delete contacts with address and zipcode fields starting with 'Test Address ' and '12345' respectively
    db.execute("DELETE FROM contacts WHERE address LIKE 'Test Address %'")
    db.execute("DELETE FROM contacts WHERE zipcode LIKE '12345%'")
    db.commit()
    print('Test contacts have been deleted from the database.')
    db.close()

if __name__ == '__main__':
    clear_test_contacts()

