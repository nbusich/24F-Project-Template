SELECT c.description, c.lastChange, a.firstname, a.lastname
                    FROM changes c
                        JOIN administrator a ON c.changerID = a.id
                    ORDER BY lastChange DESC
                    LIMIT 10;