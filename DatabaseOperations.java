```java
package com.plus.appzenx;

import io.appwrite.Client;
import io.appwrite.services.Database;
import java.util.HashMap;
import java.util.Map;

public class DatabaseOperations {

    private Client client;
    private Database database;

    public DatabaseOperations(Client client) {
        this.client = client;
        this.database = new Database(client);
    }

    public void createRecord(String collectionId, Map<String, Object> data) {
        try {
            database.createDocument(collectionId, data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void readRecord(String collectionId, String documentId) {
        try {
            database.getDocument(collectionId, documentId);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void updateRecord(String collectionId, String documentId, Map<String, Object> data) {
        try {
            database.updateDocument(collectionId, documentId, data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void deleteRecord(String collectionId, String documentId) {
        try {
            database.deleteDocument(collectionId, documentId);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```